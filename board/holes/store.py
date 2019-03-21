from board.holes.hole import Hole


class Store(Hole):
    def __init__(self, row: int, column: int, amount: int, side: str):
        super().__init__(row, column, amount, side)
        self.text = f'{self.side} store\n{amount}'

    def update(self, updated_amount: int):
        self.text = f'{self.side} store\n0{self.amount}'
