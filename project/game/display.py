from colorama import Fore, Back, Style
from .board import Board

class Display:
    @staticmethod
    def show_welcome():
        print(f"\n{Fore.YELLOW}=== ¡Bienvenido al Ta-Te-Ti Moderno! ==={Style.RESET_ALL}")
        print(f"{Fore.LIGHTBLUE_EX}Jugador 1: X{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}Jugador 2: O{Style.RESET_ALL}\n")
    
    @staticmethod
    def show_board(board: Board):
        print("\n")
        for i, row in enumerate(board.board):
            print(f"{Fore.WHITE}  {board.get_symbol_color(row[0])} │ {board.get_symbol_color(row[1])} │ {board.get_symbol_color(row[2])} ")
            if i < 2:
                print(f"{Fore.WHITE}────┼───┼────")
        print("\n")
    
    @staticmethod
    def show_turn(player: str):
        color = Fore.CYAN if player == 'X' else Fore.MAGENTA
        print(f"{color}Turno del jugador {player}{Style.RESET_ALL}")
    
    @staticmethod
    def show_winner(winner: str):
        color = Fore.CYAN if winner == 'X' else Fore.MAGENTA
        print(f"\n{color}¡Felicitaciones! ¡Ganó el jugador {winner}!{Style.RESET_ALL}")
    
    @staticmethod
    def show_draw():
        print(f"\n{Fore.YELLOW}¡Empate! El juego ha terminado.{Style.RESET_ALL}")
    
    @staticmethod
    def show_invalid_move():
        print(f"\n{Fore.RED}Movimiento inválido. Intenta nuevamente.{Style.RESET_ALL}")
    
    @staticmethod
    def get_move() -> tuple:
        try:
            print(f"{Fore.GREEN}Ingresa tu movimiento (fila columna), ejemplo: 1 2{Style.RESET_ALL}")
            row, col = map(int, input().split())
            return row - 1, col - 1
        except ValueError:
            return -1, -1