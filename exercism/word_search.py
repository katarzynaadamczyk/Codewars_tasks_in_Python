''' exercise word search '''


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def reverse(self):
        self.x, self.y = self.y, self.x
        return self

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
    point_changes = {HORIZONTAL: lambda point1, point2: point1 + point2,
                     VERTICAL: lambda point1, point2: (point1 + point2).reverse(),
                     DIAGONAL_LEFT_TO_RIGHT: lambda point1, point2: point1 + point2, # TODO
                     DIAGONAL_RIGHT_TO_LEFT: lambda point1, point2: point1 + point2} # TODO
    
    def __init__(self, puzzle):
        if not self.check(puzzle):
            raise ValueError('Wrong size of puzzle')
        self.puzzle = puzzle

    def search(self, word):
        word_reversed = word[::-1]
        for type_ in WordSearch.point_changes.keys():
            for point, line in self.generate_lines(type_):
                x_ = line.find(word)
                if x_ >= 0:
                    return (WordSearch.point_changes[type_](point, Point(x_, 0)), WordSearch.point_changes[type_](point, Point(len(word) - 1 + x_, 0)))
                x_ = line.find(word_reversed)
                if x_ >= 0:
                    return (WordSearch.point_changes[type_](point, Point(len(word) - 1 + x_, 0)), WordSearch.point_changes[type_](point, Point(x_, 0)))
        return None

    def generate_lines(self, type_):
        if type_ == WordSearch.HORIZONTAL:
            for y, line in enumerate(self.puzzle):
                yield Point(0, y), line
        if type_ == WordSearch.VERTICAL:
            for x in range(len(self.puzzle[0])):
                yield Point(0, x), ''.join([self.puzzle[y][x] for y in range(len(self.puzzle))])
        if type_ == WordSearch.DIAGONAL_LEFT_TO_RIGHT:
            x, y = len(self.puzzle[0]) - 1, 0
            while y < len(self.puzzle):
                yield Point(x, y), ''.join([self.puzzle[y_][x_] for x_, y_ in zip(range(x, len(self.puzzle[0])), range(y, len(self.puzzle)))])
                x -= 1
                if x < 0:
                    x = 0
                    y += 1
                    
        if type_ == WordSearch.DIAGONAL_RIGHT_TO_LEFT:
            # TODO
            yield Point(0, 0), 'abc'    
    
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
    