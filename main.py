import random
from util import mp3FromPhrase, textToSpeech, deleteFilesInFolder, joinAudio
import random

random.seed(0)

OLD_AGE = 100 # difference between time and age after which a word is considered old and has to be repeated

intros = ["intro1", "intro2", "intro3"]
# introduction = ["Listen to the way you would say _", "Now, let's learn how to say _", "The way to say _ is", "Listen and repeat the following which means"]
# Listen closely one more time 

# starters = ["How do you say ", "Let's hear you say "]
starters = ["starter1", "starter2"]


currDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/'
audioDir = currDir + "audio/"

phrases = []

def compile(path: str):
    chapterName = path.split('.')[0]
    with open(f"{currDir}output/{chapterName}.order", 'a') as order:
        with open(path, 'r') as file:
            lines = file.readlines()
            lineNumber = 0
            # look through each line
            for line in lines:
                # inject mp3
                if (line.startswith('$')):
                    write_line(order, line[1:-1])
                # define word/phrase
                elif (line.startswith('|')):
                    try:
                        line.index('=')
                    except ValueError:
                        raise Exception(f"No '=' found in line {lineNumber}")

                    # Swiss German phrase    
                    phrase = line[1:line.index('=')]
                    # English phrase
                    translation = line[line.index('=')+1:]

                    # introduce the phrase
                    write_line(order, f"global/{random.choice(intros)}")  
                    textToSpeech(translation, f"translate_{phrase}")
                    write_line(order, f"/generated/translate_{phrase}")

                    try:
                        phrase.index('-')
                        write_line(order, f"generated/{mp3FromPhrase(phrase)}")
                    except ValueError:
                        write_line(order, f"words/{phrase}")

                    phrases.append({"english": translation, "audio": phrase, "introduced": False, "dependencies": phrase.split('-'), "mentioned": 0})
                # text to speech comment
                elif (line.startswith('#')):
                    textToSpeech(line[1:], f"comment{lineNumber}")
                    write_line(order, f"/generated/comment{lineNumber}")
                
                lineNumber += 1

    for phrase in phrases:
        print(phrase)

    return chapterName

def build(chapterName):
    with open (f"audio/generated/{chapterName}.order", 'r') as file:
        # get audio segments in order
        audios = [AudioSegment.from_mp3(audioDir + line.replace("\n", ".mp3")) for line in file.readlines()]

        # combine
        final = reduce(lambda a, b: a.append(AudioSegment.silent(duration=500) + b, crossfade=40), audios)
    
        # export
        final.export(f"{currDir}output/{chapterName}.mp3", format="mp3")

def clean():
    deleteFilesInFolder(audioDir + "generated")


def write_line(file, line):
    file.write(line + "\n")

build(compile("chapter1.txt"))
clean()