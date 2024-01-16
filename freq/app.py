import pygame as pg

from freq.colors import BLACK
from freq.content import Content
from freq.wave import Wave


class App:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.FPS = 60
        self.SCREEN = pg.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pg.time.Clock()
        self.running = False
        self.dt: float = 1 / self.FPS
        self.content: Content = Content()

    def run(self):
        self.running = True
        while self.running:
            self._handle_event()
            self._update()
            self.SCREEN.fill(BLACK)
            self._render()
            pg.display.update()
            self.dt = self.clock.tick(self.FPS) / 1000

    def _handle_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def _render(self):
        self.content.render(self.SCREEN)

    def _update(self):
        self.content.update(self.dt)
