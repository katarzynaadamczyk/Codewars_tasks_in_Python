''' exercise Go Counting '''

import queue

BLACK = 'B'
WHITE = 'W'
NONE = ''

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if not (0 <= y < len(self.board) and 0 <= x < len(self.board[y])):
            raise ValueError("Invalid coordinate")
        coordinates_to_be_checked, territory_set, boundaries = queue.SimpleQueue(), set(), set()
        if self.board[y][x] == ' ':
            coordinates_to_be_checked.put((x, y))
        while not coordinates_to_be_checked.empty():
            actual_coordinate = coordinates_to_be_checked.get()
            territory_set.add(actual_coordinate)
            for new_coordinate in self.where_to_go(actual_coordinate):
                if 0 <= new_coordinate[1] < len(self.board) and 0 <= new_coordinate[0] < len(self.board[new_coordinate[1]]):
                    if self.board[new_coordinate[1]][new_coordinate[0]] == ' ':
                        if new_coordinate not in territory_set:
                            coordinates_to_be_checked.put(new_coordinate)
                    else:
                        boundaries.add(self.board[new_coordinate[1]][new_coordinate[0]])
        stone = NONE
        if len(boundaries) == 1:
            stone = list(boundaries)[0]
        return stone, territory_set

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        territories_dict, coordinates_set = {WHITE: set(), BLACK: set(), NONE: set()}, set()
        for y in range(len(self.board)):
            for x, value in enumerate(self.board[y]):
                if value == ' ' and (x, y) not in coordinates_set:
                    stone, coordinates = self.territory(x=x, y=y)
                    territories_dict[stone] = territories_dict[stone].union(coordinates)
                    coordinates_set = coordinates_set.union(coordinates)
        return territories_dict
    
    def where_to_go(self, coordinate):
        yield (-1 + coordinate[0], coordinate[1])
        yield (1 + coordinate[0], coordinate[1])
        yield (coordinate[0], coordinate[1] - 1)
        yield (coordinate[0], coordinate[1] + 1)


def main():
    board = Board(["  B  ", " B B ", "B W B", " W W ", "  W  "])
    stone, territory = board.territory(x=0, y=1)
    print(stone)
    print(territory)
    print(board.territories())
        
if __name__ == '__main__':
    main()
    
    