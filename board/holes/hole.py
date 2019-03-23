from kivy.uix.label import Label


class Hole(Label):
    def __init__(self, side: str, **kwargs):
        """Instantiate a hole.
        :param side: which player owns this hole
        """
        super().__init__(**kwargs)
        self.side = side

    def update(self, updated_amount: int):
        """Update the amount of stones in the hole.
        :param updated_amount: the amount to update
        """
        self.text = str(updated_amount)
