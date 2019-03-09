import time
from typing import List

from kivy.app import App
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

from board.holes.pit import Pit
from board.holes.store import Store


class GraphicsBoard(GridLayout):
    """Class representing the board, with the graphics."""

    def __init__(self):
        super(GraphicsBoard, self).__init__()
        self.rows = 2
        self.cols = 8
        self.info_label = Label(text='Welcome!')
        self._initialize_holes()

    def _initialize_holes(self):
        """Insert the stores and pits in the board."""
        self.upper_store = Store(0, 0, 0, 'upper')
        self.add_widget(self.upper_store)

        self.upper_pits = []
        self.lower_pits = []
        for column in range(1, self.cols):
            self.upper_pits.append(Pit(0, column, 4, 'upper'))
        for column in range(self.cols - 1):
            self.lower_pits.append(Pit(1, column, 4, 'lower'))

        for pit in self.upper_pits + self.lower_pits:
            self.add_widget(pit)

        self.lower_store = Store(1, self.cols, 0, 'lower')
        self.add_widget(self.lower_store)

    def update(self, upper_pits: List[int], lower_pits: List[int], upper_store: int, lower_store: int):
        for pit, updated_amount in zip(self.upper_pits, upper_pits):
            pit.amount = updated_amount
        for pit, updated_amount in zip(self.upper_pits, lower_pits):
            pit.amount = updated_amount
        self.upper_store.amount = upper_store
        self.lower_store.amount = lower_store

    def get_press(self):
        all_pits = self.upper_pits + self.lower_pits

        for pit in all_pits:
            pit.enable_press()

        was_pressed = False
        while not was_pressed:
            for pit in all_pits:
                if pit.is_pressed:
                    pressed_pit_side = pit.side
                    pressed_pit_number = pit.column
                    break
            time.sleep(0.01)

        for pit in all_pits:
            pit.disable_press()

        return pressed_pit_side, pressed_pit_number


class Mancala(App):
    def build(self):
        self.title = 'Mancala'
        return GraphicsBoard()


if __name__ == '__main__':
    Config.set('graphics', 'window_state', 'maximized')  # Configure the board to open in full screen
    Config.set('kivy', 'exit_on_escape', '1')  # Make the game close if the Esc key in pressed
    Mancala().run()
