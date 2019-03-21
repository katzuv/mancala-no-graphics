from board.holes.hole import Hole


class Store(Hole):
    def __init__(self, row: int, column: int, amount: int, side: str):
        super().__init__(row, column, amount, side, 'images/store.png')