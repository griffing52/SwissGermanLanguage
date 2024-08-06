from pydub import AudioSegment

currDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage'

# sound = AudioSegment.from_mp3("/audio/conversation1.mp3")
# sound = AudioSegment.from_mp3("C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/audio/conversation1.mp3")
mier = AudioSegment.from_mp3(currDir+"/audio/mier.mp3")
hend = AudioSegment.from_mp3(currDir+"/audio/hend.mp3")
luscht = AudioSegment.from_mp3(currDir+"/audio/luscht.mp3")

# len() and slicing are in milliseconds
# halfway_point = len(sound) / 2
# second_half = sound[halfway_point:]

# # Concatenation is just adding
# second_half_3_times = second_half + second_half + second_half

output = mier + hend + luscht

# # writing mp3 files is a one liner
output.export(currDir+"/audio/file.mp3", format="mp3")

# add silence
# two_sec_silence = AudioSegment.silent(duration=2000)
# sound_with_gap = sound[:1000] + two_sec_silence + sound[1000:]