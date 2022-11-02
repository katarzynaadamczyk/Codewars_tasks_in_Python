''' exercise word search '''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return '(' + str(self.x) + ', ' + str(self.y) + ')'



class WordSearch:
    
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL_LEFT_TO_RIGHT = 2
    DIAGONAL_RIGHT_TO_LEFT = 3
    point_changes = {HORIZONTAL: lambda x, y, x_: Point(x + x_, y),
                     VERTICAL: lambda x, y, x_: Point(y + x_, x), 
                     DIAGONAL_LEFT_TO_RIGHT: lambda x, y, x_: Point(x + x_, y + x_), 
                     DIAGONAL_RIGHT_TO_LEFT: lambda x, y: Point()} # TODO
    
    def __init__(self, puzzle):
        if not self.check(puzzle):
            raise ValueError('Wrong size of puzzle')
        self.puzzle = puzzle

    def search(self, word):
        word_reversed = word[::-1]
        for type_ in WordSearch.point_changes.keys():
            for y, x, line in self.generate_lines(type_):
                x_ = line.find(word)
                if x_ >= 0:
                    return (WordSearch.point_changes[type_](x, y, x_), WordSearch.point_changes[type_](x + len(word) - 1, y, x_))
                x_ = line.find(word_reversed)
                if x_ >= 0:
                    return (WordSearch.point_changes[type_](x + len(word) - 1, y, x_), WordSearch.point_changes[type_](x, y, x_))
        return None

    def generate_lines(self, type_):
        if type_ == WordSearch.HORIZONTAL:
            for y, line in enumerate(self.puzzle):
                yield y, 0, line
        if type_ == WordSearch.VERTICAL:
            for x in range(len(self.puzzle[0])):
                yield x, 0, ''.join([self.puzzle[y][x] for y in range(len(self.puzzle))])
        if type_ == WordSearch.DIAGONAL_LEFT_TO_RIGHT:
            x, y = len(self.puzzle[0]) - 1, 0
            while y < len(self.puzzle):
                yield y, x, ''.join([self.puzzle[y_][x_] for x_, y_ in zip(range(x, len(self.puzzle[0])), range(y, len(self.puzzle)))])
                x -= 1
                if x < 0:
                    x = 0
                    y += 1
                    
        if type_ == WordSearch.DIAGONAL_RIGHT_TO_LEFT:
            # TODO
            yield 0, 0, 'abc'    
    
    def check(self, puzzle):
        if len(puzzle) == 0:
            return False
        line_len = [len(line) for line in puzzle]
        if min(line_len) != max(line_len):
            return False
        return True
    
def main():
    guess = WordSearch(['abc', 'xyz'])
    for line in guess.generate_lines(WordSearch.DIAGONAL_LEFT_TO_RIGHT):
        print(line)
    puzzle = WordSearch(
    [
        "jefblpepre",
        "camdcimgtc",
        "oivokprjsm",
        "pbwasqroua",
        "rixilelhrs",
        "wolcqlirpc",
        "screeaumgr",
        "alxhpburyi",
        "jalaycalmp",
        "clojurermt",
    ]
)
    print(puzzle.search("clojure"), (Point(0, 9), Point(6, 9)))
    print(puzzle.search("elixir"), (Point(5, 4), Point(0, 4)))
    print(puzzle.search("ecmascript"), (Point(9, 0), Point(9, 9)))
    print(puzzle.search("rust"), (Point(8, 4), Point(8, 1)))

if __name__ == '__main__':
    main()
    