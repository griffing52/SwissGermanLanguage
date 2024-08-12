import random

random.seed(0)

OLD_AGE = 100 # difference between time and age after which a word is considered old and has to be repeated

class Audio:
    def __init__(self, filename):
        self.filename = filename

    def getAudioFile(self):
        return f"{self.filename}.mp3"

    def __str__(self):
        return f"{self.filename}.mp3"

    def __repr__(self):
        return self.filename

class Word(Audio):
    def __init__(self, word, translation):
        Audio.__init__(self, word)
        self.word = word
        self.translation = translation
        self.rep = 0 # how many times the word has been repeated
        self.age = 0 # the last time the word was repeated

    def __str__(self):
        return f"{self.word}, rep: {self.rep}, age: {self.age}" 

    def __repr__(self):
        return f"{self.word} - {self.translation}"

class Phrase(Audio):
    def __init__(self, phrase, translation):
        self.phrase = phrase
        self.translation = translation
        self.rep = 0
        self.dependencies = phrase.split(' ')
        self.complexity = len(self.dependencies) + 1
        Audio.__init__(self, '-'.join(self.dependencies))

    def __str__(self):
        return f"{self.phrase}, {self.complexity}"

    def __repr__(self):
        return f"{self.phrase} - {self.translation}"

words = [Word("mier", "we"), Word("gond", "go"), Word("uf", "to or for"), Word("Italie", "Italy"), Word("hend", "have"), Word("luscht", "desire or lust"), Word("das", "this"), Word("wuchenendi", "weekend"), Word("weil", "because"), Word("Pizza", "pizza"), Word("und", "and"), Word("SpaghettiBolognese", "Spaghetti Bolognese")]
wordDict = {word.word: word for word in words}

phrases = [Phrase("mier gond", "we are going"), Phrase("mier gond uf Italie", "we are going to Italy"), Phrase("mier hend luscht", "we want to"), Phrase("mier gond das wuchenendi uf Italie", "we are going this weekend to Italie"), Phrase("mier gond uf Italie weil mier luscht hend", "we are going to Italy because we want to"), Phrase("Pizza und SpaghettiBolognese", "Pizza and Spaghetti Bolognese"), Phrase("mier hend luscht uf Pizza und SpaghettiBolognese", "we want Pizza and Spaghetti Bolognese"), Phrase("mier gond weil mier luscht hend uf Pizza und SpaghettiBolognese", "we are going because we want Pizza and Spaghetti Bolognese"), Phrase("mier gond das wuchenendi uf Italie weil mier luscht hend uf Pizza und SpaghettiBolognese", "we are going to Italy this weekend because we want Pizza and Spaghetti Bolognese")]
# phrases = [Phrase("mier gond das wuchenendi uf Italie weil mier luscht hend uf Pizza und SpaghettiBolognese", "we are going to Italy this weekend because we want Pizza and Spaghetti Bolognese")]

# TODO make sure to increase everytime a word/phase is written
time = 0

for phrase in phrases:
    print(phrase)
    phrase.rep += 1
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
                wordDict[word].rep += 1
                print(wordDict[word])

            time += 1
            wordDict[word].rep += 1
            print(wordDict[word])
            wordDict[word].age = time


    time += 1
    print(phrase)
    phrase.rep += 1