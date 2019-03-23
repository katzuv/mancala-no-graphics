from board.board import Board


class Game:

    def __init__(self, upper_player, lower_player):
        """Instantiate a Mancala game."""
        self.board = Board()

        self._upper_player = upper_player
        self._lower_player = lower_player

        self._current_player = self._upper_player

    def play(self) -> None:
        """Play the game."""
        while True:
            if self._turn():
                return

    def _swap_players_if_needed(self) -> None:
        """Swap the players if the board indicates it is needed."""
        self._current_player = self._upper_player if self.board.current_player == 'upper' else self._lower_player

    def _turn(self) -> bool:
        """Run the game and return whether it has ended.
        :return: whether the game has ended
        """
        pit_number = self._current_player.turn(self.board)
        if self.board.move(pit_number):
            self._print_winner_or_tie()
            return True
        # self._swap_players_if_needed()

        return False

    def _print_winner_or_tie(self):
        """Print the side of the winner or tie if a tie occurred."""
        print(self.board)
        winner = self.board.winner()
        if winner != 'tie':
            print(f'{winner.capitalize()} player won!')
        else:
            print('Both players have the same amount of stones, tie.')
