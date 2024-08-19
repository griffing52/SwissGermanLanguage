from util import Word

with open("input/words.txt", 'r') as wordFile:
    lines = wordFile.readlines()
    for line in lines:
        if line == "\n":
            continue
        foreign, english = line.split("=")
        # remove new line
        english = english[:-1]
        print(Word(foreign, english))