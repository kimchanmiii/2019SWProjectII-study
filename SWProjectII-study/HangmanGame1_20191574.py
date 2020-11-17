class Guess:

    def __init__(self, word):
        self.secretWord=word
        self.guessedChars=set([])
        self.numTries=0
        self.currentStatus="_"*len(word)

    def display(self):

        print("Current:",self.currentStatus)
        print("Tries",self.numTries)


    def guess(self, character):
        self.guessedChars.add(character)
        if character not in self.secretWord:
            self.numTries += 1
            return False
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == character:
                self.currentStatus = self.currentStatus[:i] + character + self.currentStatus[i + 1:]
        if self.currentStatus!=self.secretWord:
            return False
        return True
