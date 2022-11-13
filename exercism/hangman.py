''' game hangman - exercise from exercism '''

# Game status categories
# Change the values as you see fit
STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.word = word
        self.status = STATUS_ONGOING
        self.guessed = set()

    def guess(self, char):
        if self.remaining_guesses < 0 or self.get_masked_word() == self.word:
            raise ValueError('The game has already ended.')
        if char in self.word and char not in self.guessed:
            self.guessed.add(char)
        else:
            self.remaining_guesses -= 1
        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        if self.remaining_guesses == 0 and self.status == STATUS_ONGOING:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(self.generate_masked_word())

    def get_status(self):
        return self.status
    
    def generate_masked_word(self):
        for letter in self.word:
            yield '_' if letter not in self.guessed else letter
