from abc import ABC, abstractmethod

from board.board_representation import BoardRepresentation


class PlayerBase(ABC):
    def __init__(self, side: str):
        """Instantiate a player.
        :param side: the side of the player ("upper" or "down")
        """
        self.side = side

    @abstractmethod
    def turn(self, board: BoardRepresentation) -> int:
        """Make a turn.
        :param board: the current game's board
        :return: choice of player
        """
        pass
