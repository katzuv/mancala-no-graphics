from board.board_representation import BoardRepresentation
from players.player_base import PlayerBase


class Console(PlayerBase):
    def turn(self, board: BoardRepresentation) -> int:
        """Get the human player's choice.
        :param board: current board
        :return: choice of pit number
        """
        while True:
            print(f'\n{board}')
            pit_number = input(f'{self.side.capitalize()} player, enter pit number: ')
            if '.' in pit_number:
                print('Dots are not supported')
                continue
            try:
                pit_number = int(pit_number) - 1
            except ValueError:
                print(f'{pit_number} is not a number')
                continue
            if not (0 <= pit_number <= 5):
                print(f'Pit number {pit_number + 1} is out of bounds')
                continue
            if board.is_pit_empty(self.side, pit_number):
                print(f'Pit number {pit_number + 1} is empty')
                continue
            break
        return pit_number
