from pydub import AudioSegment

currDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage'

# sound = AudioSegment.from_mp3("/audio/conversation1.mp3")
# sound = AudioSegment.from_mp3("C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/audio/conversation1.mp3")
# a = AudioSegment.from_mp3(currDir+"/audio/global/silence.mp3")
# b = AudioSegment.from_mp3(currDir+"/audio/global/starter2.mp3")
# hend = AudioSegment.from_mp3(currDir+"/audio/hend.mp3")/
# luscht = AudioSegment.from_mp3(currDir+"/audio/luscht.mp3")

# len() and slicing are in milliseconds
# halfway_point = len(sound) / 2
# second_half = sound[halfway_point:]

# # Concatenation is just adding
# second_half_3_times = second_half + second_half + second_half

# output = a + b

# # writing mp3 files is a one liner
# output.export(currDir+"/audio/global/silent_starter2.mp3", format="mp3")

# add silence
# two_sec_silence = AudioSegment.silent(duration=2000)
# sound_with_gap = sound[:1000] + two_sec_silence + sound[1000:]

AudioSegment.silent(duration=1000).export(currDir+"/audio/global/silence.mp3", format="mp3")