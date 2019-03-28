import copy
import random

from board.board_representation import BoardRepresentation
from players.player_base import PlayerBase


class AI(PlayerBase):
    def turn(self, board: BoardRepresentation) -> int:
        pits = [index for index, pit in enumerate(board.lower_pits) if pit > 0]
        last_in_store = [index for index, pit in enumerate(pits) if pit + index == 6]
        # if last_in_store:
        #     return random.choice(last_in_store)

        last_in_empty = [index for index in pits if self._causes_last_in_empty(index, board)]
        print(last_in_empty)
        if last_in_empty:
            return random.choice(last_in_empty)
        return random.choice([index for index, pit in enumerate(board.lower_pits) if pit > 0])

    @staticmethod
    def _causes_last_in_empty(pit_number: int, board: BoardRepresentation) -> None:
        """
        Deposit the stones in the pits.
        :param pit_number: the player's choosing
        :param board: current board
        :return: whether
        """
        board = copy.deepcopy(board)
        player_pits, other_pits = board.lower_pits, board.upper_pits
        amount_to_deposit = player_pits[pit_number]
        player_pits[pit_number] = 0
        all_pits = player_pits + [0] + other_pits
        index = pit_number + 1
        while amount_to_deposit > 0:
            amount_to_deposit -= 1
            all_pits[index] += 1  # Increment the amount of stones in this pit
            index += 1  # Advance to the next pit
            if index == 13:  # If completed a cycle,
                index = 0  # start it again

        return 0 <= index <= 5 and all_pits[index] == 1


if __name__ == '__main__':
    ai = AI('lower')
    board = BoardRepresentation([0] * 6, [0, 1, 0, 0, 0, 0], 0, 0)
    ai.turn(board)
