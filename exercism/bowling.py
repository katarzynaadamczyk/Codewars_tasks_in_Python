''' exercise bowling game '''

class BowlingGame:
    BONUS = 11
    ENDING = BONUS + 1
    PINS_MAX = 10
    
    def __init__(self):
        self.frames_dict = {x: [] for x in range(1, BowlingGame.ENDING + 1)}
        self.actual_frame = 1
        self.throws_max = 2
        self.pins_left = BowlingGame.PINS_MAX
        

    def roll(self, pins):
        if pins < 0 or pins > self.pins_left:
            raise ValueError("invalid fill balls")
        if self.actual_frame < BowlingGame.BONUS:
            self.frames_dict[self.actual_frame].append(pins)
            self.pins_left -= pins
            if len(self.frames_dict[self.actual_frame]) == self.throws_max or sum(self.frames_dict[self.actual_frame]) == BowlingGame.PINS_MAX:
                self.actual_frame += 1
                self.pins_left = BowlingGame.PINS_MAX
            if self.actual_frame == BowlingGame.BONUS:
                if sum(self.frames_dict[self.actual_frame - 1]) == BowlingGame.PINS_MAX:
                    self.throws_max = 2 if len(self.frames_dict[self.actual_frame - 1]) == 1 else 1
                else:
                    self.actual_frame += 1
        elif self.actual_frame == BowlingGame.BONUS:
            self.frames_dict[self.actual_frame].append(pins)
            self.pins_left -= pins
            self.throws_max -= 1
            if self.throws_max == 0:
                self.actual_frame += 1
            if self.pins_left == 0:
                self.pins_left = BowlingGame.PINS_MAX
        else:
            raise IndexError("cannot throw bonus with an open tenth frame") 

    def score(self):
        if self.actual_frame < BowlingGame.ENDING:
            raise IndexError("cannot throw bonus with an open tenth frame") 
        return self.count_score()
    
    def count_score(self):
        score = 0
        for frame, throws in self.frames_dict.items():
            if frame >= BowlingGame.BONUS:
                break
            act_sum = sum(throws)
            if act_sum == 10:
                act_sum += self.get_sum_of_next_two_throws(frame) if len(throws) == 1 else self.get_value_of_next_throw(frame)
            score += act_sum
        return score
    
    def get_sum_of_next_two_throws(self, frame):
        return sum(self.frames_dict[frame + 1]) if len(self.frames_dict[frame + 1]) == 2 else sum([self.frames_dict[frame + 1][0], self.frames_dict[frame + 2][0]])
    
    def get_value_of_next_throw(self, frame):
        return self.frames_dict[frame + 1][0]
    
    
                
def main():
    rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 0, 1]
    game = BowlingGame()
    for roll in rolls:
        game.roll(roll)
    print(game.score())
        
if __name__ == '__main__':
    main()
    