from board.board_representation import BoardRepresentation
from board.graphics_board import GraphicsBoard
from players.player_base import PlayerBase


class Graphics(PlayerBase):
    def __init__(self, side: str, graphics_board: GraphicsBoard):
        super().__init__(side)
        self.graphics_board = graphics_board

    def turn(self, board: BoardRepresentation) -> int:
        while True:
            side, number = self.graphics_board.get_press()
            if side != self.side:
                print('sides')
            if not board.is_pit_empty(self, number):
                print('empty')
            return number
