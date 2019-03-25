from typing import List, Tuple

from board.board_representation import BoardRepresentation
from players import AI


class Board:
    def __init__(self):
        """Instantiate a Mancala board."""
        self.ai_player = self.ai_player = AI('lower')
        self._upper_pits = [4] * 6
        self._lower_pits = [4] * 6
        self._upper_store = 0
        self._lower_store = 0
        self.extra_turn = False
        self.current_player = 'upper'
        self.has_match_ended = False

    def __str__(self) -> str:
        """
        :return: a string describing the current board
        """
        numbers_row = ' '.join(f'{i}\t' for i in range(1, 7))
        upper_row = '\t '.join(str(pit) for pit in self._upper_pits)
        lower_row = '\t '.join(str(pit) for pit in self._lower_pits)
        return f'{numbers_row}\n{upper_row}\n{lower_row}\nUp store: {self._upper_store}, Down store: {self._lower_store}'''

    def _is_match_over(self) -> bool:
        """
        :return: whether the match has ended
        """
        return all(pit == 0 for pit in self._upper_pits) or all(pit == 0 for pit in self._lower_pits)

    def _swap_players_if_needed(self):
        if not self.extra_turn:
            self.current_player = 'lower' if self.current_player == 'upper' else 'upper'

    def move(self, pit_number: int):
        """Make a move and return whether the match is over.
        :param pit_number: last pit number the player took stones from
        """
        self._deposit(pit_number)
        self.has_match_ended = self._is_match_over()
        self._empty_pits_when_match_ends()

    def _empty_pits_when_match_ends(self):
        if self.has_match_ended:
            self._upper_store += sum(self._upper_pits)
            for index in range(len(self._upper_pits)):
                self._upper_pits[index] = 0
            self._lower_store += sum(self._lower_pits)
            for index in range(len(self._lower_pits)):
                self._lower_pits[index] = 0

    def winner(self):
        if self._upper_store > self._lower_store:
            return 'upper'
        elif self._lower_store > self._upper_store:
            return 'lower'
        return 'tie'

    def _deposit(self, pit_number: int) -> None:
        """
        Deposit the stones in the pits.
        :param pit_number: the player's choosing
        """
        player_pits, other_pits = self.sort_pits()
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

        if index == 7:  # If the last stone fell in the store, give the player an extra turn
            self.extra_turn = True
        else:
            self.extra_turn = False
        self._update_stores(all_pits[6])
        all_pits = all_pits[:6] + all_pits[7:]  # Remove the store from the list of pits
        self._update_pits(all_pits)
        player_pits = all_pits[:6]
        self._handle_last_in_empty(index, player_pits)
        self._swap_players_if_needed()

    def _handle_last_in_empty(self, index: int, player_pits: List[int]) -> None:
        """Handle the rule that if the player drops their last stone in an empty pit on their side, they capture that
        stone and any stones in the pit directly opposite.
        :param index: pit index where the last stone was dropped
        :param player_pits: pits of both players
        """
        index -= 1
        if 0 <= index <= 5 and player_pits[index] == 1:
            other_pits = self.sort_pits()[1]
            store_addition = 1 + other_pits[5 - index]
            player_pits[index] = 0
            other_pits[5 - index] = 0
            self._update_stores(store_addition)
            self._update_pits(player_pits + other_pits)

    def _update_stores(self, store_addition) -> None:
        if self.current_player == 'upper':
            self._upper_store += store_addition
        else:
            self._lower_store += store_addition

    def sort_pits(self) -> Tuple[List[int], List[int]]:
        """Sort the pits before each round (if the current player is the upper one, upper pits are returned first)"""
        if self.current_player == 'upper':
            return self._upper_pits, self._lower_pits
        return self._lower_pits, self._upper_pits

    def _update_pits(self, all_pits: List[int]):
        player_pits = all_pits[:len(all_pits) // 2]
        other_pits = all_pits[len(all_pits) // 2:]
        if self.current_player == 'upper':
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
        return BoardRepresentation(self._upper_pits, self._lower_pits, self._upper_store, self._lower_store)
