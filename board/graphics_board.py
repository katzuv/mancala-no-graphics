import logging

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from board.board import Board
from board.board_representation import BoardRepresentation
from board.holes.pit import Pit
from board.holes.store import Store


class GraphicsBoard(GridLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        super(GraphicsBoard, self).__init__()
        self.rows = 3
        self.cols = 8
        self.info_label = Label(text='Welcome!')
        self.board = Board()
        self._initialize_board()

    def _initialize_board(self):
        """Insert the stores and pits in the board."""
        self.upper_store = Store('upper')
        self.add_widget(Widget())
        self.upper_pits = []
        self.upper_labels = []
        self.lower_pits = []
        self.lower_labels = []
        for pit_number in range(6):
            self.upper_pits.append(Pit(pit_number, 'upper'))
        for upper_pit in self.upper_pits:
            self.add_widget(upper_pit)
        self.add_widget(self.upper_store)
        self.lower_store = Store('lower')
        self.add_widget(self.lower_store)
        for pit_number in range(6):
            self.lower_pits.append(Pit(5 - pit_number, 'lower'))

        for lower_pit in self.lower_pits:
            self.add_widget(lower_pit)
        self.info_label = Label(font_size='20sp')
        self._update_info_label()
        self.add_widget(Widget())
        self.add_widget(self.info_label)

    def update(self, board: BoardRepresentation):
        logging.info('Updating board')
        for pit, updated_amount in zip(self.upper_pits, board.upper_pits):
            pit.update(updated_amount)
        for pit, updated_amount in zip(self.lower_pits, reversed(board.lower_pits)):
            pit.update(updated_amount)
        self.upper_store.update(board.upper_store)
        self.lower_store.update(board.lower_store)
        self._update_info_label()

    def _update_info_label(self):
        if self.board.has_match_ended:
            endgame_string = self._endgame_string(self.board.winner())
            logging.info(endgame_string)
            self.info_label.text = 100 * ' ' + endgame_string
        else:
            self.info_label.text = f'{100 * " "}{"Human" if self.board.current_player == "upper" else "Computer"} is playing'

    @staticmethod
    def _endgame_string(winner: str):
        if winner == 'tie':
            return 'Match ended with a tie.'
        return f'The winner is the {winner} player!'
