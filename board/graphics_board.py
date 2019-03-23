import logging

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from board.board import Board
from board.board_representation import BoardRepresentation
from board.holes.ai_pit import AIPit
from board.holes.human_player_pit import HumanPlayerPit
from board.holes.store import Store


class GraphicsBoard(GridLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        super(GraphicsBoard, self).__init__()
        self.rows = 2
        self.cols = 7
        self.info_label = Label(text='Welcome!')
        self.board = Board()
        self._initialize_board()

    def _initialize_board(self):
        """Insert the stores and pits in the board."""
        self.upper_store = Store('upper')

        self.upper_pits = []
        self.upper_labels = []
        self.lower_pits = []
        self.lower_labels = []
        for pit_number in range(6):
            self.upper_pits.append(HumanPlayerPit(pit_number))
        for upper_pit in self.upper_pits:
            self.add_widget(upper_pit)
        self.add_widget(self.upper_store)
        self.lower_store = Store('lower')
        self.add_widget(self.lower_store)
        for pit_number in range(6):
            self.lower_pits.append(AIPit(5 - pit_number))

        for lower_pit in self.lower_pits:
            self.add_widget(lower_pit)

    def update(self, board: BoardRepresentation):
        logging.info('Updating board')
        for pit, updated_amount in zip(self.upper_pits, board.upper_pits):
            pit.update(updated_amount)
        for pit, updated_amount in zip(self.lower_pits, board.lower_pits):
            pit.update(updated_amount)
        self.upper_store.update(board.upper_store)
        self.lower_store.update(board.lower_store)
