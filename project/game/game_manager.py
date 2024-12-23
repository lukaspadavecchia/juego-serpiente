from .board import Board
from .display import Display

class GameManager:
    def __init__(self):
        self.board = Board()
        self.display = Display()
    
    def start_game(self):
        self.display.show_welcome()
        
        while True:
            self.display.show_board(self.board)
            self.display.show_turn(self.board.current_player)
            
            row, col = self.display.get_move()
            if row == -1 or not self.board.make_move(row, col):
                self.display.show_invalid_move()
                continue
            
            winner = self.board.get_winner()
            if winner:
                self.display.show_board(self.board)
                self.display.show_winner(winner)
                break
            
            if self.board.is_full():
                self.display.show_board(self.board)
                self.display.show_draw()
                break
            
            self.board.switch_player()