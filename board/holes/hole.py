from kivy.uix.label import Label


class Hole(Label):
    def __init__(self, row: int, column: int, side: str):
        """Instantiate a hole.
        :param row: line of the hole
        :param column: column of the hole
        :param amount: amount of stones in hole
        :param side: which player owns this hole
        """
        super().__init__()
        self.row = row
        self.column = column
        self.side = side

    def update(self, updated_amount: int):
        """Update the text of the hole
        :param updated_amount: the amount to update
        """
        self.text = str(updated_amount)
