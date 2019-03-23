from game import Game
from mancala import Mancala
from players import AI, Console
from players.graphics import Graphics


def main():
    """Main function running the game."""
    # mancala = Mancala()
    print('Welcome to Mancala!\n')
    # game = Game(player_type_chooser(mancala, 'upper'), player_type_chooser(mancala, 'lower'), mancala)
    game = Game(Console('upper'), Console('lower'))
    game.play()


def player_type_chooser(mancala: Mancala, player_side: str):
    """Return the type of a player.
    :return: the type chosen of a player
    """
    while True:
        player_type = input(
            f'Enter the type of the {player_side} player: 1 for Human or 3 for AI: ')
        if player_type == '1':
            return Console(player_side)
        if player_type == '2':
            return AI(player_side)
        if player_type == '3':
            return Graphics(player_side, mancala.board)
        else:
            print('You did not enter a valid number')


if __name__ == '__main__':
    main()

