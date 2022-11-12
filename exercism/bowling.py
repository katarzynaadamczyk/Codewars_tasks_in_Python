''' exercise bowling game '''

class BowlingGame:
    def __init__(self):
        self.__score__ = 0
        self.__frame__ = 1
        self.__pins_left__ = 10
        self.__throw_no__ = 1
        self.__no_of_throws_for_multiplier__ = [0]
        self.__no_of_throws_left__ = 20

    def roll(self, pins):
        if pins < 0 or pins > self.__pins_left__:
            raise ValueError("invalid fill balls")
      #  if self.__frame__ > 10:
      #      raise IndexError("cannot throw bonus with an open tenth frame")
        self.__score__ += len(self.__no_of_throws_for_multiplier__) * pins
        self.__pins_left__ -= pins
        if pins == 10 and self.__throw_no__ == 1:
            self.__frame__ += 1
            self.__pins_left__ = 10
            if self.__frame__ < 10:
                self.__no_of_throws_left__ -= 2
                self.__no_of_throws_for_multiplier__.append(3)
            elif self.__frame__ >= 10:
                self.__no_of_throws_left__ -= 1
            elif self.__frame__ == 10:
                print(self.__frame__)
                print(self.__no_of_throws_left__)
        elif self.__pins_left__ == 0:
            self.__frame__ += 1
            self.__throw_no__ = 1
            self.__pins_left__ = 10
            if self.__frame__ < 10:
                self.__no_of_throws_for_multiplier__.append(2)
                self.__no_of_throws_left__ -= 1
            elif self.__frame__ > 10:
                self.__no_of_throws_left__ -= 1
        elif self.__throw_no__ == 2:
            self.__frame__ += 1
            self.__throw_no__ = 1
            self.__pins_left__ = 10
            self.__no_of_throws_left__ -= 1
        else:
            self.__no_of_throws_left__ -= 1
            self.__throw_no__ += 1
        self.actualize_multipliers()

    def score(self):
        #if self.__no_of_throws_left__ > 0:
        #    raise IndexError("cannot throw bonus with an open tenth frame") 
        print(self.__no_of_throws_left__)
        return self.__score__
    
    def actualize_multipliers(self):
        for index in range(len(self.__no_of_throws_for_multiplier__) - 1, 0, -1):
            self.__no_of_throws_for_multiplier__[index] -= 1
            if self.__no_of_throws_for_multiplier__[index] == 0:
                del self.__no_of_throws_for_multiplier__[index]
                
def main():
    rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 1]
    game = BowlingGame()
    for roll in rolls:
        game.roll(roll)
        print(game.score())
        
if __name__ == '__main__':
    main()
    