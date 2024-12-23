from colorama import init
from game.game_manager import GameManager

def main():
    # Initialize colorama for Windows compatibility
    init()
    
    # Create and start the game
    game = GameManager()
    game.start_game()
    
    # Ask to play again
    while True:
        play_again = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if play_again == 's':
            game = GameManager()
            game.start_game()
        elif play_again == 'n':
            print("\n¡Gracias por jugar! ¡Hasta la próxima!")
            break

if __name__ == "__main__":
    main()