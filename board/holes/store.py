from board.holes.hole import Hole


class Store(Hole):
    def __init__(self, side: str):
        super().__init__(side)
        self.text = f'{self.side.capitalize()} store: 0'

    def update(self, updated_amount: int):
        self.text = f'{self.side.capitalize()} store: {updated_amount}'
