''' exercise connect '''

possible_moves = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]

class ConnectGame:
    def __init__(self, board):
        self.board = [x.split() for x in board.split('\n')]
        print(self.board)

    def get_winner(self):
        pass


def main():
    new_game = ConnectGame("""O O O X
                                X . . X
                                  X . . X
                                    X O O O""")

if __name__ == '__main__':
    main()
    