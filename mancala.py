from kivy import Config
from kivy.app import App

from board.graphics_board import GraphicsBoard


class Mancala(App):
    def __init__(self):
        super().__init__()
        self.board = GraphicsBoard()

    def build(self):
        self.title = 'Mancala'
        return self.board

    def build_config(self, config):
        Config.set('graphics', 'window_state', 'maximized')
        Config.set('kivy', 'exit_on_escape', '1')


if __name__ == '__main__':
    Mancala().run()
