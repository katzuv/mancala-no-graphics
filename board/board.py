from typing import List, Tuple

from board.board_representation import BoardRepresentation


class Board:
    def __init__(self):
        """Instantiate a Mancala board."""
        self._upper_pits = [4] * 6
        self._lower_pits = [4] * 6
        self._upper_store = 0
        self._lower_store = 0
        self.extra_turn = False

    def __str__(self) -> str:
        """
        :return: a string describing the current board
        """
        numbers_row = ' '.join(f'{i}\t' for i in range(1, 7))
        upper_row = '\t '.join(str(pit) for pit in self._upper_pits)
        lower_row = '\t '.join(str(pit) for pit in self._lower_pits)
        return f'{numbers_row}\n{upper_row}\n{lower_row}\nUp store: {self._upper_store}, Down store: {self._lower_store}'''

    def _is_game_over(self) -> bool:
        """
        :return: whether the game has ended
        """
        if all(pit == 0 for pit in self._upper_pits):
            return True
        return all(pit == 0 for pit in self._lower_pits)

    def move(self, player_side: str, pit_number: int):
        self._deposit(player_side, pit_number)
        return self._is_game_over()

    def winner(self):
        upper_sum = sum(self._upper_pits) + self._upper_store
        lower_sum = sum(self._lower_pits) + self._lower_store
        if upper_sum > lower_sum:
            return 'upper'
        elif lower_sum > upper_sum:
            return 'lower'
        return 'tie'

    def _deposit(self, player_side: str, pit_number: int) -> None:
        """
        Deposit the stones in the pits.
        :param player_side: current player's side
        :param pit_number: the player's choosing
        """
        player_pits, other_pits = self.sort_pits(player_side)
        amount_to_deposit = player_pits[pit_number]
        player_pits[pit_number] = 0
        all_pits = player_pits + [0] + other_pits
        index = pit_number + 1
        while amount_to_deposit > 0:
            amount_to_deposit -= 1
            all_pits[index] += 1  # Increment the amount of stones in this pit
            index += 1  # Advance to the next pit
            if index == 12:  # If completed a cycle,
                index = 0  # start it again

        if index == 7:  # If the last stone fell in the store, give the player an extra turn
            self.extra_turn = True
        else:
            self.extra_turn = False
        self._update_stores(player_side, all_pits[6])
        all_pits = all_pits[:6] + all_pits[7:]  # Remove the store from the list of pits
        self._update_pits(player_side, all_pits)
        player_pits = all_pits[:6]
        self._handle_last_in_empty(player_side, index, player_pits)

    def _handle_last_in_empty(self, player_side: str, index: int, player_pits: List[int]) -> None:
        """Handle the rule that if the player drops their last stone in an empty pit on their side, they capture that
        stone and any stones in the pit directly opposite.
        :param player_side: current player
        :param index: pit index where the last stone was dropped
        :param player_pits: pits of both players
        """
        index -= 1
        if 0 <= index <= 5 and player_pits[index] == 1:
            store_addition = self._upper_pits[index] + self._lower_pits[index]
            self._upper_pits[index] = 0
            self._lower_pits[index] = 0
            self._update_stores(player_side, store_addition)

    def _update_stores(self, player_side: str, store_addition) -> None:
        if player_side == 'upper':
            self._upper_store += store_addition
        else:
            self._lower_store += store_addition

    def sort_pits(self, player_side) -> Tuple[List[int], List[int]]:
        """Sort the pits before each round (if the current player is the upper one, upper pits are returned first)"""
        if player_side == 'upper':
            return self._upper_pits, self._lower_pits
        return self._lower_pits, self._upper_pits

    def _update_pits(self, player_side: str, all_pits: List[int]):
        player_pits = all_pits[:len(all_pits) // 2]
        other_pits = all_pits[len(all_pits) // 2:]
        if player_side == 'upper':
            self._upper_pits = player_pits
            self._lower_pits = other_pits
        else:
            self._upper_pits = other_pits
            self._lower_pits = player_pits

    def is_pit_empty(self, player_side: str, pit_number: int) -> bool:
        pits = self._upper_pits if player_side == 'upper' else self._lower_pits
        return pits[pit_number] == 0

    def representation(self) -> BoardRepresentation:
        """Return a representation of the board for the players."""
        return BoardRepresentation(self._upper_pits, self._lower_pits)
