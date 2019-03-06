from typing import List

from kivy.app import App
from kivy.config import Config
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


class Pit(ButtonBehavior, Image):
    def __init__(self, row: int, column: int, board, amount: int, source='..\\images\\pit.png'):
        """
        Instantiate a pit.
        :param row: line of the pit
        :type row: int
        :param column: column of the pit
        :type column: int
        :param board: the board which the pit is in
        :type board: Board
        """
        super().__init__()
        self.row = row
        self.column = column
        self.source = source
        self.board = board
        self.amount = amount

    def on_press(self):
        raise NotImplementedError


class GraphicsBoard(GridLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        super(GraphicsBoard, self).__init__()
        self.rows = 2
        self.cols = 8
        self._initialize_pits()

    def _initialize_pits(self):
        """Insert the stores and pits in the board."""
        self.upper_store = Pit(0, 0, self, 0, '..\\images\\store.png')
        self.add_widget(self.upper_store)

        self.upper_pits = []
        self.lower_pits = []
        for column in range(1, self.cols):
            self.upper_pits.append(Pit(0, column, self, 4))
        for column in range(self.cols - 1):
            self.lower_pits.append(Pit(1, column, self, 4))

        for pit in self.upper_pits + self.lower_pits:
            self.add_widget(pit)

        self.lower_store = Pit(1, self.cols, self, 0, '..\\images\\store.png')
        self.add_widget(self.lower_store)

    def update(self, upper_pits: List[int], lower_pits: List[int], upper_store: int, lower_store: int):
        for pit, updated_amount in zip(self.upper_pits, upper_pits):
            pit.amount = updated_amount
        for pit, updated_amount in zip(self.upper_pits, lower_pits):
            pit.amount = updated_amount
        self.upper_store.amount = upper_store
        self.lower_store.amount = lower_store

    def _has_game_ended(self):
        """
        Return whether the game has ended. The game ends when all pits of one player are empty.
        :return: whether the game has ended
        :rtype: bool
        """
        for pit in self.upper_pits:
            if pit.amount != 0:
                break
        else:
            return True
        for pit in self.lower_pits:
            if pit.amount != 0:
                return False
        return True


class Mancala(App):
    def build(self):
        self.title = 'Mancala'
        board = Board()
        return GraphicsBoard(board)


if __name__ == '__main__':
    Config.set('graphics', 'window_state', 'maximized')  # Configure the board to open in full screen
    Config.set('kivy', 'exit_on_escape', '1')  # Make the game close if the Esc key in pressed
    Mancala().run()
