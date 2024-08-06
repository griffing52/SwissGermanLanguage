from pydub import AudioSegment
from functools import reduce

from gtts import gTTS

import os, shutil

audioDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/audio/'

# mp3FromPhrase("mier-gond-weil-mier-luscht-hend-uf-Pizza-und-SpaghettiBolognese")
def mp3FromPhrase(phrase: str):
    audioFiles = [AudioSegment.from_mp3(f"{audioDir}words/{word}.mp3") for word in phrase.split('-')]
    # final = reduce(lambda a, b: a.append(b, crossfade=100), audioFiles)
    final = reduce(lambda a, b: a.append(b, crossfade=40), audioFiles)
    # final = reduce(lambda a, b: a + AudioSegment.silent(duration=13) + b, audioFiles)

    final.export(f"{audioDir}generated/{phrase}.mp3", format="mp3")

    return phrase


def textToSpeech(phrase: str, fileName: str):
    audio = gTTS(text=phrase, lang='en', slow=False)

    # Saving the converted audio in a mp3 file named
    audio.save(f"{audioDir}/generated/{fileName}.mp3")


def joinAudio(audios: list, crossfade: int, silence: int):
    return reduce(lambda a, b: a.append(AudioSegment.silent(duration=silence) + b, crossfade=crossfade), audios)


def deleteFilesInFolder(folder: str):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))