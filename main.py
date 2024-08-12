import random
from util import mp3FromPhrase, textToSpeech, deleteFilesInFolder, joinAudio
from pydub import AudioSegment
from functools import reduce

import os

from util import Word, Phrase, Audio

random.seed(0)

OLD_AGE = 100 # difference between time and age after which a word is considered old and has to be repeated

intros = ["intro1", "intro2", "intro3"]
# introduction = ["Listen to the way you would say _", "Now, let's learn how to say _", "The way to say _ is", "Listen and repeat the following which means"]
# Listen closely one more time 

# starters = ["How do you say ", "Let's hear you say "]
starters = ["starter1", "starter2"]


currDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/'
audioDir = currDir + "audio/"

def compile(path: str, wordPath: str = "words.txt"):
    wordDict = {}
    phrases = []

    # TODO make sure to increase everytime a word/phase is written
    time = 0

    with open(wordPath, 'r') as wordFile:
        lines = wordFile.readlines()
        for line in lines:
            foreign, english = line.split("=")
            # remove new line
            english = english[:-1]
            wordDict[foreign] =  Word(foreign, english)
            textToSpeech(english, f"translated_{foreign}")

    chapterName = path.split('.')[0]
    
    with open(path, 'r') as file:
        lines = file.readlines()
        lineNumber = 0
        # look through each line
        for line in lines:
            # inject mp3
            if (line.startswith('$')):
                phrases.append(Audio(line[1:-1]))
                # write_line(order, line[1:-1])
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

                phraseFileName = phrase.replace(' ','-')
                # introduce the phrase
                # write_line(order, f"global/{random.choice(intros)}")  
                if not os.path.isfile(f"{currDir}audio/generated/translated_{phraseFileName}.mp3"):
                    textToSpeech(translation, f"translated_{phraseFileName}")

                if not os.path.isfile(f"{currDir}audio/generated/{phraseFileName}.mp3"):
                    mp3FromPhrase(phraseFileName)
                # write_line(order, f"/generated/translate_{phrase}")

                # try:
                #     phrase.index('-')
                #     write_line(order, f"generated/{mp3FromPhrase(phrase)}")
                # except ValueError:
                #     write_line(order, f"words/{phrase}")

                phrases.append(Phrase(phrase, translation))
                
            # text to speech comment
            elif (line.startswith('#')):
                textToSpeech(line[1:], f"comment{lineNumber}")
                phrases.append(Audio(f"generated/comment{lineNumber}"))
                # write_line(order, f"/generated/comment{lineNumber}")
            
            lineNumber += 1

    with open(f"{currDir}output/{chapterName}.order", 'a') as order:
        for phrase in phrases:
            # inject mp3 and skip the rest if pure audio file (comments and injected mp3s)
            if (phrase.complexity == 0):
                write_line(order, phrase.getAudioFile())
                continue
            
            writeWordAudioSegment(order, phrase, time, intros)
            # write_line(order, f"global/{random.choice(intros)}")
            # write_line(order, f"generated/translated_{phrase.getFileName()}")
            # write_line(order, phrase.getAudioFile())
            time += 1

            dependenciesPassed = 0

            while dependenciesPassed < len(phrase.dependencies):
                dependenciesPassed = 0
                for word in phrase.dependencies:
                    if word not in wordDict:
                        raise Exception(f"Word {word} not found in dictionary")

                    if wordDict[word].rep >= phrase.complexity and time - wordDict[word].age < OLD_AGE:
                        dependenciesPassed += 1
                        continue

                    # probability of choosing word gets lower the more it's repeated
                    # 0 -> 1
                    # 1 -> 0.77
                    # 2 -> 0.63
                    # 3 -> 0.53
                    prob = 1 / (0.35 * wordDict[word].rep + 1)

                    # skip word if not chosen
                    if not random.random() < prob:
                        continue

                    if wordDict[word].rep == 0:
                        time += 1
                        writeWordAudioSegment(order, wordDict[word], time, intros)
                        # wordDict[word].rep += 1
                        # write_line(order, f"global/{random.choice(intros)}") 
                        # write_line(order, f"generated/translated_{wordDict[word].getFileName()}")
                        # write_line(order, wordDict[word].getAudioFile())

                    time += 1
                    writeWordAudioSegment(order, wordDict[word], time)
                    # wordDict[word].rep += 1
                    # write_line(order, f"global/{random.choice(starters)}") 
                    # write_line(order, wordDict[word].getTranslatedAudioFile())
                    # write_line(order, wordDict[word].getAudioFile())
                    # wordDict[word].age = time


            time += 1
            writeWordAudioSegment(order, phrase, time)
            # write_line(order, f"global/{random.choice(starters)}") 
            # write_line(order, phrase.getTranslatedAudioFile())
            # write_line(order, phrase.getAudioFile())
            # phrase.rep += 1

    return chapterName


def writeWordAudioSegment(file, audio: Audio, time, preAudio = starters):
    audio.rep += 1
    write_line(order, f"global/{random.choice(preAudio)}") 
    write_line(order, audio.getTranslatedAudioFile())
    write_line(order, audio.getAudioFile())
    audio.age = time

def build(chapterName):
    with open (f"output/{chapterName}.order", 'r') as file:
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

# build(compile("lessons.txt"))
build("lessons")
# compile("lessons.txt")
# clean()