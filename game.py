from board.board import Board


class Game:

    def __init__(self, upper_player_type: type, lower_player_type: type):
        self.board = Board()

        self._upper_player = upper_player_type()
        self._lower_player = lower_player_type()

        self._current_player = self._upper_player

    def play(self) -> None:
        """Play the game."""
        while True:
            if self._turn():
                return
            self._swap_players_if_needed()

    def _swap_players_if_needed(self) -> None:
        """Swap the players if the board indicates it is needed."""
        if not self.board.extra_turn:
            if self._current_player == self._upper_player:
                self._current_player = self._lower_player
            else:
                self._current_player = self._upper_player

    def _turn(self):
        pit_number = self._current_player.turn(self.board.representation())

        def play():
            while True:
                player = swap_players_if_needed(board, player)
                pit_number = get_player_choice(board, player)
                if board.move(player, pit_number):
                    winner = board.winner().capitalize()
                    if winner != 'tie':
                        print(f'{winner} won!')
                    else:
                        print('Both players have the same amount of stones, tie.')
                    return
                print()
