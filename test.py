from random_words import RandomWords


class Sentence:
    def __init__(self):
        rw = RandomWords()

        self.words = rw.random_words(count=50)

        self.new = [" ".join(self.words)]

        self.sentence = ""
        for i in self.new:
            self.sentence += i



    def show(self):
        return self.words

    def print_words(self):
        print(self.words)