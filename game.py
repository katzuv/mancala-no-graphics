from board.board import Board


class Game:

    def __init__(self, upper_player_type, lower_player_type):
        """Instantiate a Mancala game.
        :param upper_player_type: type of the upper player
        :param lower_player_type: type of the lower player
        """
        self.board = Board()

        self._upper_player = upper_player_type('upper')
        self._lower_player = lower_player_type('lower')

        self._current_player = self._upper_player

    def play(self) -> None:
        """Play the game."""
        while True:
            if self._turn():
                return

    def _swap_players_if_needed(self) -> None:
        """Swap the players if the board indicates it is needed."""
        if not self.board.extra_turn:
            if self._current_player == self._upper_player:
                self._current_player = self._lower_player
            else:
                self._current_player = self._upper_player

    def _turn(self) -> bool:
        """Run the game and return whether it has ended.
        :return: whether the game has ended
        """
        pit_number = self._current_player.turn(self.board)
        if self.board.move(self._current_player.side, pit_number):
            self._handle_endgame()
            return True
        self._swap_players_if_needed()

        return False

    def _handle_endgame(self):
        print(self.board)
        winner = self.board.winner()
        if winner != 'tie':
            print(f'{winner.capitalize()} player won!')
        else:
            print('Both players have the same amount of stones, tie.')
