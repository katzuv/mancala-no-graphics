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
        upper_row = '\t '.join(str(pit) for pit in self._upper_pits)
        lower_row = '\t '.join(str(pit) for pit in self._lower_pits)
        return f'{upper_row}\n{lower_row}\nUp store: {self._upper_store}, Down store: {self._lower_store}'''

    def _is_game_over(self) -> bool:
        """
        :return: whether the game has ended
        """
        if all(pit == 0 for pit in self._upper_pits):
            return True
        return all(pit == 0 for pit in self._lower_pits)

    def move(self, player, pit_number):
        self._deposit(player, pit_number)
        return self._is_game_over()

    def winner(self):
        upper_sum = sum(self._upper_pits) + self._upper_store
        lower_sum = sum(self._lower_pits) + self._lower_store
        return 'upper' if upper_sum > lower_sum else 'lower'

    def _deposit(self, player, pit_number):
        player_pits = self._upper_pits
        other_pits = self._lower_pits
        if player == 'lower':
            player_pits, other_pits = other_pits, player_pits
        amount = player_pits[pit_number]
        player_pits[pit_number] = 0
        all_pits = player_pits + other_pits
        store_addition = 0
        index = pit_number + 1
        while amount > 0:
            if index == 6:
                store_addition += 1
                amount -= 1
                if amount == 0:  # If the last stone fell in the player's store, they are granted an additional turn
                    break
            all_pits[index] += 1
            index += 1
            amount -= 1
            if index == 12:
                index = 0

        self._update_pits(all_pits)

        if 0 <= index <= 5 and self.is_pit_empty(player, index):
            amount = self._upper_pits[index] + self._lower_pits[index]
            self._upper_pits[index] = 0
            self._lower_pits[index] = 0
            store_addition += amount

        if index == 6:  # If the last stone fell in the player's store, they are granted an additional turn
            self.extra_turn = True
        else:
            self.extra_turn = False

        if player == 'upper':
            self._upper_store += store_addition
        else:
            self._lower_store += store_addition
        self._update_pits(all_pits)
        if player == 'lower':
            self._upper_pits, self._lower_pits = self._lower_pits, self._upper_pits

    def _update_pits(self, all_pits):
        self._upper_pits = all_pits[:len(all_pits) // 2]
        self._lower_pits = all_pits[len(all_pits) // 2:]

    def is_pit_empty(self, player: str, pit_number: int) -> bool:
        pits = self._upper_pits if player == 'upper' else self._lower_pits
        return pits[pit_number] == 0


def play():
    board = Board()
    player = 'lower'
    while True:
        if not board.extra_turn:
            player = 'upper' if player == 'lower' else 'lower'
        while True:
            print(' '.join(f'{i}\t' for i in range(1, 7)))
            print(board)
            pit_number = input(f'{player.capitalize()} player, enter pit number: ')
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
            if board.is_pit_empty(player, pit_number):
                print(f'Pit number {pit_number + 1} is empty')
                continue
            break
        if board.move(player, pit_number):
            print(f'{board.winner().capitalize()} won!')
            return
        print()


if __name__ == '__main__':
    play()
