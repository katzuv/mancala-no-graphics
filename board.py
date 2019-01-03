class Board:
    def __init__(self):  # , up_player: Player, second_player: Player):
        """
        Instantiate a Mancala board.
        :param up_player: the player whose row is the upper row
        :param second_player: the player whose row is the lower row
        """
        self._upper_pits = [0] * 6
        self._lower_pits = [0] * 6
        self._up_store = 0
        self._down_store = 0

    def __str__(self) -> str:
        """
        :return: a string describing the current board
        """
        upper_row = '\t'.join(str(pit) for pit in self._upper_pits)
        lower_row = '\t'.join(str(pit) for pit in self._lower_pits)
        return f'''{self._up_store}      {upper_row}
{lower_row}     {self._down_store}'''

    def _is_game_over(self) -> bool:
        """
        :return: whether the game has ended
        """
        if all(pit == 0 for pit in self._upper_pits):
            return True
        return all(pit == 0 for pit in self._lower_pits)

    def move(self): pass


if __name__ == '__main__':
    print(Board())
