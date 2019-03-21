from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from board.board import Board
from board.holes.pit import Pit
from board.holes.store import Store


class GraphicsBoard(GridLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        super(GraphicsBoard, self).__init__()
        self.rows = 2
        self.cols = 8
        self.info_label = Label(text='Welcome!')
        self.board = Board()
        self._initialize_board()

    def _initialize_board(self):
        """Insert the stores and pits in the board."""
        self.upper_store = Store(0, 0, 0, 'upper')
        self.add_widget(self.upper_store)

        self.upper_pits = []
        self.upper_labels = []
        self.lower_pits = []
        self.lower_labels = []
        for column in range(1, self.cols):
            self.upper_pits.append(Pit(0, column, 4, 'upper', True, self.board))
        for column in range(self.cols - 1):
            self.lower_pits.append(Pit(1, column, 4, 'lower', False, self.board))

        for pit in self.upper_pits + self.lower_pits:
            self.add_widget(pit)

        self.lower_store = Store(1, self.cols, 0, 'lower')
        self.add_widget(self.lower_store)

    def update(self, board):
        for pit, updated_amount in zip(self.upper_pits, board.upper_pits):
            pit.update(updated_amount)
        for pit, updated_amount in zip(self.upper_pits, board.lower_pits):
            pit.update(updated_amount)
        self.upper_store.update(board.upper_store)
        self.lower_store.update(board.lower_store)


class Mancala(App):
    def build(self):
        self.title = 'Mancala'
        return GraphicsBoard()


if __name__ == '__main__':
    Config.set('graphics', 'window_state', 'maximized')  # Configure the board to open in full screen
    Config.set('kivy', 'exit_on_escape', '1')  # Make the game close if the Esc key in pressed
    Mancala().run()
