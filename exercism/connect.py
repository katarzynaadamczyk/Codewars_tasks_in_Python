''' exercise connect '''
import queue

possible_moves = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

class ConnectGame:
    def __init__(self, board):
        self.board = [x.split() for x in board.split('\n')]
        self.player_O = 'O'
        self.player_X = 'X'
        self.possible_moves = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

    def get_winner(self):
        if self.check_if_player_wins(self.player_O):
            return self.player_O
        self.transform_board()
        if self.check_if_player_wins(self.player_X):
            return self.player_X
        return ''

    def check_if_player_wins(self, player):
        tiles_to_check = queue.SimpleQueue()
        tiles_checked = set()
        for x, value in enumerate(self.board[0]):
            if value == player:
                tiles_to_check.put((0, x))
        while not tiles_to_check.empty():
            actual_tile = tiles_to_check.get()
            if actual_tile[0] == len(self.board) - 1:
                return True
            tiles_checked.add(actual_tile)
            for move in self.possible_moves:
                new_tile = (actual_tile[0] + move[0], actual_tile[1] + move[1])
                if 0 <= new_tile[0] < len(self.board) and 0 <= new_tile[1] < len(self.board[0]):
                    if new_tile not in tiles_checked and self.board[new_tile[0]][new_tile[1]] == player:
                        tiles_to_check.put(new_tile)
        return False
    
    def transform_board(self):
        self.board = list(list(x) for x in zip(*self.board))

def main():
    new_game = ConnectGame("""O O O X
                                X . . X
                                  X . . X
                                    X O O O""")
    print(new_game.get_winner(), 'should equal ""')
    
    
if __name__ == '__main__':
    main()
    