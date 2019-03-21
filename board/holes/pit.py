import logging

from kivy.uix.behaviors import ButtonBehavior

from board.board import Board
from board.holes.hole import Hole


class Pit(ButtonBehavior, Hole):
    def __init__(self, row: int, column: int, amount: int, side: str, is_pressable: bool, board: Board, **kwargs):
        super().__init__(row=row, column=column, amount=amount, side=side, **kwargs)
        self.board = board
        self.text = str(amount)
        self._is_pressable = is_pressable

    def on_press(self):
        if not self._is_pressable:
            return
        if self.amount == 0:
            logging.error("pit is empty")

        self._turn('upper', self.column)
        if self.board.current_player == 'lower':
            self._turn('lower', self.board.ai_player.turn(self.board))

    def _turn(self, side, pit_number):
        if self.board.move(side, pit_number):
            for pit in self.parent.upper_pits:
                pit._is_pressable = False
            winner = self.board.winner()
            if winner == 'tie':
                logging.info(f'Match ended with a tie.')
            else:
                logging.info(f'The winner is the {winner} player!')
        self.parent.update(self.board.representation())

    def enable_press(self):
        self._is_pressable = True

    def disable_press(self):
        self._is_pressable = False
