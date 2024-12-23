from colorama import Fore, Style
from typing import List, Optional, Tuple

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        
    def make_move(self, row: int, col: int) -> bool:
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            return True
        return False
    
    def is_valid_move(self, row: int, col: int) -> bool:
        if 0 <= row < 3 and 0 <= col < 3:
            return self.board[row][col] == ' '
        return False
    
    def get_winner(self) -> Optional[str]:
        # Check rows
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col]) and self.board[0][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) and self.board[0][0] != ' ':
            return self.board[0][0]
        if (self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[0][2] != ' ':
            return self.board[0][2]
        
        return None
    
    def is_full(self) -> bool:
        return all(cell != ' ' for row in self.board for cell in row)
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def get_symbol_color(self, symbol: str) -> str:
        if symbol == 'X':
            return f"{Fore.CYAN}{symbol}{Style.RESET_ALL}"
        elif symbol == 'O':
            return f"{Fore.MAGENTA}{symbol}{Style.RESET_ALL}"
        return symbol