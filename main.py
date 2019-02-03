from game import Game
from players import AI, Human


def main():
    """Main function running the game."""
    while True:
        print('Welcome to Mancala!\n')
        game = Game(player_type_chooser('upper'), player_type_chooser('lower'))
        game.play()
        if input("Would you like to play again? Enter 'Y' if yes, anything else if not: ").upper() != 'Y':
            print('Thanks for playing! Hope you enjoyed, see you next time :-)')
            return


def player_type_chooser(player_side: str):
    """Return the type of a player.
    :return: the type chosen of a player
    """
    while True:
        player_type = input(
            f'Enter the type of the {player_side} player: 1 for Human or 3 for AI: ')
        if player_type == '1':
            return Human
        if player_type == '2':
            return AI
        else:
            print('You did not enter a valid number')


if __name__ == '__main__':
    main()
