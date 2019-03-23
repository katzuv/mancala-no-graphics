from board.holes.hole import Hole


class AIPit(Hole):
    def __init__(self, pit_number: int, **kwargs):
        super().__init__(side='lower', **kwargs)
        self.pit_number = pit_number
        self.text = '4'
