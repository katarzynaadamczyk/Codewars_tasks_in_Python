''' exercise bowling game '''

class BowlingGame:
    BONUS = 11
    ENDING = BONUS + 1
    
    def __init__(self):
        self.frames_dict = {x: [] for x in range(1, BowlingGame.ENDING + 1)}
        self.actual_frame = 1
        self.bonus = 0
        self.throws_max = 2
        self.pins_left = 10
        

    def roll(self, pins):
        if pins < 0 or pins > self.pins_left:
            raise ValueError("invalid fill balls")
        if self.actual_frame < BowlingGame.BONUS:
            self.frames_dict[self.actual_frame].append(pins)
            if sum(self.frames_dict[self.actual_frame]) == 10:
                self.actual_frame +=1
                self.pins_left = 10
            elif len(self.frames_dict[self.actual_frame]) == 2:
                self.actual_frame +=1
                self.pins_left = 10
            else:
                self.pins_left -= pins
                self.bonus = self.bonus - 1 if self.bonus > 0 else 0
        elif self.actual_frame == BowlingGame.BONUS and self.bonus > 0:
            self.frames_dict[self.actual_frame].append(pins)
            self.bonus -= 1
            if self.bonus <= 0:
                self.actual_frame += 1
        else:
            raise IndexError("cannot throw bonus with an open tenth frame") 

    def score(self):
        if self.actual_frame < BowlingGame.ENDING:
            raise IndexError("cannot throw bonus with an open tenth frame") 
        return self.count_score()
    
    def count_score(self):
        for key, val in self.frames_dict.items():
            print(key, ':', val)
        return sum([sum(x) for x in self.frames_dict.values()])
    
                
def main():
    rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 1]
    game = BowlingGame()
    for roll in rolls:
        game.roll(roll)
        print(game.score())
        
if __name__ == '__main__':
    main()
    