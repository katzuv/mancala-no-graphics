import logging
import time

from kivy.uix.behaviors import ButtonBehavior

from board.holes.hole import Hole


class Pit(ButtonBehavior, Hole):
    def __init__(self, pit_number: int, side, **kwargs):
        super().__init__(side=side, **kwargs)
        self.text = '4'
        self.pit_number = pit_number

    def on_press(self):
        if self.parent.board.has_match_ended:
            logging.info('Match has ended')
            return
        if self.parent.board.current_player != self.side:
            logging.warning('Not your turn!')
            return
        if self.side == 'upper':
            if int(self.text) < 1:
                logging.warning(f'Pit number {self.pit_number} is empty')
                return
            choice = self.pit_number
        else:
            choice = self.parent.board.ai_player.turn(self.parent.board.representation())
        self._turn(choice)

    def _turn(self, pit_number):
        logging.info(f'{self.side.capitalize()}: pit number {self.pit_number}')
        self.parent.board.move(pit_number)
        self.parent.update(self.parent.board.representation())
        time.sleep(0.25)
