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



class WordSearch:
    
    HORIZONTAL = 0
    VERTICAL = 1
    DIAGONAL_LEFT_TO_RIGHT = 2
    DIAGONAL_RIGHT_TO_LEFT = 3
    point_changes = {HORIZONTAL: lambda x, y: Point(x, y),
                     VERTICAL: lambda x, y: Point(y, x), 
                     DIAGONAL_LEFT_TO_RIGHT: lambda x, y: Point(), # TODO
                     DIAGONAL_RIGHT_TO_LEFT: lambda x, y: Point()} # TODO
    
    def __init__(self, puzzle):
        if not self.check(puzzle):
            raise ValueError('Wrong size of puzzle')
        self.puzzle = puzzle

    def search(self, word):
        word_reversed = word[::-1]
        for type_ in WordSearch.point_changes.keys():
            for y, line in self.generate_lines(type_):
                x = line.find(word)
                if x >= 0:
                    return (WordSearch.point_changes[type_](x, y), WordSearch.point_changes[type_](x + len(word) - 1, y))
                x = line.find(word_reversed)
                if x >= 0:
                    return (WordSearch.point_changes[type_](x + len(word) - 1, y), WordSearch.point_changes[type_](x, y))
        return None

    def generate_lines(self, type_):
        if type_ == WordSearch.HORIZONTAL:
            for y, line in enumerate(self.puzzle):
                yield y, line
        if type_ == WordSearch.VERTICAL:
            for x in range(len(self.puzzle[0])):
                yield x, ''.join([self.puzzle[y][x] for y in range(len(self.puzzle))])
        if type_ == WordSearch.DIAGONAL_LEFT_TO_RIGHT:
            # TODO
            yield 'abc'
        if type_ == WordSearch.DIAGONAL_RIGHT_TO_LEFT:
            # TODO
            yield 'abc'    
    
    def check(self, puzzle):
        if len(puzzle) == 0:
            return False
        line_len = [len(line) for line in puzzle]
        if min(line_len) != max(line_len):
            return False
        return True
    
    