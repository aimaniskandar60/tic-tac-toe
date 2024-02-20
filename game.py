import sys 
sys.dont_write_bytecode = True
import time
from player import HumanPlayer, ComputerPlayer


class TicTacToe:
    def __init__(self) -> None:
        self.board = [' ' for _ in range(9)] # Single list to represent board.
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self) -> list[str]:
        return [
            i for i, spot in enumerate(self.board) if spot == ' '
        ]
    
    def empty_squares(self) -> bool:
        return ' ' in self.board
    
    def valid_move(self, square: int, letter: str) -> bool:
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square: int, letter: str) -> bool:
        # check row 
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1) * 3]
        if all([position == letter for position in row]):
            return True
        
        # check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([position == letter for position in column]):
            return True
        
        # check diagonals
        # only way to win for diagonals are for the square to be an even number.
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([position == letter for position in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([position == letter for position in diagonal2]):
                return True
            
        return False

def play(game: TicTacToe, x_player: HumanPlayer, o_player: ComputerPlayer, print_game: bool =True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter

    # While there are still empty squares on the board.
    while game.empty_squares():
        square = x_player.get_move(game) if letter == 'X' else o_player.get_move(game)

        if game.valid_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print("")

            # End game if there's a winner.
            if game.current_winner:
                if print_game:
                    print(f"{letter} wins.")
                break
            
            letter = 'O' if letter == 'X' else 'X'
        
        time.sleep(0.8)

    if print_game and not game.current_winner:
        print("It\'s a tie.")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player, True)