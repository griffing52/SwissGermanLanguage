import random

random.seed(0)

class Word:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation
        self.rep = 0 # how many times the word has been repeated
        self.age = 0 # the last time the word was repeated

    def __str__(self):
        return f"{self.word}, {self.rep}"

    def __repr__(self):
        return f"{self.word} - {self.translation}"

class Phrase:
    def __init__(self, phrase, translation):
        self.phrase = phrase
        self.translation = translation
        self.rep = 0
        self.dependencies = phrase.split(' ')
        self.complexity = len(self.dependencies) + 1

    def __str__(self):
        return f"{self.phrase}, {self.complexity}"

    def __repr__(self):
        return f"{self.phrase} - {self.translation}"

words = [Word("mier", "we"), Word("gond", "go"), Word("uf", "to or for"), Word("Italie", "Italy"), Word("hend", "have"), Word("luscht", "desire or lust"), Word("das", "this"), Word("wuchenendi", "weekend"), Word("weil", "because"), Word("Pizza", "pizza"), Word("und", "and"), Word("SpaghettiBolognese", "Spaghetti Bolognese")]
wordDict = {word.word: word for word in words}

phrases = [Phrase("mier gond", "we are going"), Phrase("mier gond uf Italie", "we are going to Italy"), Phrase("mier hend luscht", "we want to"), Phrase("mier gond das wuchenendi uf Italie", "we are going this weekend to Italie"), Phrase("mier gond uf Italie weil mier luscht hend", "we are going to Italy because we want to"), Phrase("Pizza und SpaghettiBolognese", "Pizza and Spaghetti Bolognese"), Phrase("mier hend luscht uf Pizza und SpaghettiBolognese", "we want Pizza and Spaghetti Bolognese"), Phrase("mier gond weil mier luscht hend uf Pizza und SpaghettiBolognese", "we are going because we want Pizza and Spaghetti Bolognese"), Phrase("mier gond das wuchenendi uf Italie weil mier luscht hend uf Pizza und SpaghettiBolognese", "we are going to Italy this weekend because we want Pizza and Spaghetti Bolognese")]

for phrase in phrases:
    print(phrase)
    phrase.rep += 1

    dependenciesPassed = 0

    while dependenciesPassed < len(phrase.dependencies):
        dependenciesPassed = 0
        for word in phrase.dependencies:
            if word not in wordDict:
                raise Exception(f"Word {word} not found in dictionary")

            if wordDict[word].rep >= phrase.complexity:
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
                wordDict[word].rep += 1
                print(wordDict[word])

            wordDict[word].rep += 1
            print(wordDict[word])


    print(phrase)
    phrase.rep += 1






# from functools import reduce
# from pydub import AudioSegment

# currDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/'
# audioDir = 'C:/Users/griff/Documents/Programming/Python/SwissGermanLanguage/audio/'

# with open ("audio/generated/order.data", 'r') as file:
#     audios = [AudioSegment.from_mp3(audioDir + line.replace("\n", ".mp3")) for line in file.readlines()]

#     final = reduce(lambda a, b: a.append(AudioSegment.silent(duration=500) + b, crossfade=40), audios)

#     final.export(currDir + "output/chapter1.mp3", format="mp3")