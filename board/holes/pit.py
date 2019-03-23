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
        # TODO: Disable all pits when match ends
        if self.parent.board.has_match_ended:
            logging.info('Match has ended')
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
        logging.info(f'{self.side} playing: pit number {self.pit_number}')
        if self.parent.board.move(pit_number):
            for pit in self.parent.upper_pits:
                pit.disble_press()
            winner = self.parent.board.winner()
            if winner == 'tie':
                logging.info(f'Match ended with a tie.')
            else:
                logging.info(f'The winner is the {winner} player!')
        self.parent.update(self.parent.board.representation())
        time.sleep(0.5)