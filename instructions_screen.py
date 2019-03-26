from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Screen(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 2
        self.cols = 1
        self.add_widget(Label(text='Mancala Rules', font_size='40sp', underline=False))
        self.add_widget(Label(text='''
        The Mancala board is made up of two rows of six pits each.
        A number on each pit represents the amount of stones in this pit.
        Each player owns a store where they store their stones.
        
        The game begins with one player picking up all of the stones in any one of the pit on their side.
        Moving clockwise, the player deposits one of the stones in each pit until the stones run out.
        If you run into your own store, deposit one stone in it. If you run into your opponent's store, skip it.
        If the last stone you drop is in your own store, you get a free turn.
        If the last stone you drop falls in an empty pit on your side, you capture that stone and any stones in
        the pit directly opposite.
        
        The game ends when all six pits on one side of the board are empty.
        The player who has stones on his side of the board when the game ends captures all of those stones.
        Count all the stones in each store. The winner is the player with the most stones.\n\n\n
        ''', font_size='17.5sp', valign='center', shorten=True))


class InstructionsScreen(App):
    def build(self):
        self.title = 'Instructions'
        return Screen()


if __name__ == '__main__':
    InstructionsScreen().run()
