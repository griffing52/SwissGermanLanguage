from functools import reduce
from pydub import AudioSegment

currDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/'
audioDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/audio/'

with open ("audio/generated/order.data", 'r') as file:
    audios = [AudioSegment.from_mp3(audioDir + line.replace("\n", ".mp3")) for line in file.readlines()]

    final = reduce(lambda a, b: a.append(AudioSegment.silent(duration=500) + b, crossfade=40), audios)

    final.export(currDir + "output/chapter1.mp3", format="mp3")