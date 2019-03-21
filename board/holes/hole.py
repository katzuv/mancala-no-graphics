from kivy.uix.label import Label


class Hole(Label):
    def __init__(self, row: int, column: int, amount: int, side: str, image_path: str):
        """Instantiate a hole.
        :param row: line of the hole
        :param column: column of the hole
        :param amount: amount of stones in hole
        :param side: which player owns this hole
        """
        super().__init__()
        self.row = row
        self.column = column
        self.amount = amount
        self.side = side
        self.text = '0'