import logging
import time

from kivy.uix.behaviors import ButtonBehavior

from board.holes.hole import Hole


class HumanPlayerPit(ButtonBehavior, Hole):
    def __init__(self, pit_number: int, **kwargs):
        super().__init__(side='upper', **kwargs)
        self.text = '4'
        self.pit_number = pit_number

    def on_press(self):
        # TODO: Disable all pits when match ends
        if not self.parent.board.current_player == 'upper':
            logging.warning('Not your turn!')
            return
        if int(self.text) < 1:
            logging.warning(f'Pit number {self.pit_number} is empty')
            return
        if self.parent.board.current_player == 'upper':
            self._turn(self.pit_number)
            logging.info(f'upper playing: pit number {self.pit_number}')
        while self.parent.board.current_player == 'lower':
            lower_choice = self.parent.board.ai_player.turn(self.parent.board.representation())
            logging.info(f'lower playing: pit number {lower_choice}')
            self._turn(lower_choice)

    def _turn(self, pit_number):
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
