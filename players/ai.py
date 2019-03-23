import random

from board.board_representation import BoardRepresentation
from players.player_base import PlayerBase


class AI(PlayerBase):
    def turn(self, board: BoardRepresentation) -> int:
        return random.choice([index for index, pit in enumerate(board.lower_pits) if pit > 0])
