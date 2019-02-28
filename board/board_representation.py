from typing import List


class BoardRepresentation:

    def __init__(self, upper_pits: List[int], lower_pits: List[int], upper_store: int, lower_store):
        """Instantiate a tic-tac-toe board representation.
        :param upper_pits: the current board
        """
        self.upper_pits = upper_pits
        self.lower_pits = lower_pits
        self.upper_store = upper_store
        self.lower_store = lower_store

    def __str__(self) -> str:
        """
        :return: a string describing the current board
        """

        def convert_list_of_numbers_to_string(row):
            return ' | '.join(str(number) for number in row)

        return '\n'.join(convert_list_of_numbers_to_string(row) for row in (self.upper_pits, self.lower_pits))

    def is_pit_empty(self, player, pit_number: int) -> bool:
        """
        :param player: the player to check their pits
        :param pit_number: pit to check in :player:'s row
        :return: whether that specific pit is empty
        """
        if player.side == 'upper':
            return self.upper_pits[pit_number] == 0
        return self.lower_pits[pit_number] == 0
