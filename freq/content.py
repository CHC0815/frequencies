import pygame as pg

from freq.colors import WHITE
from freq.wave import Wave


class Content:
    def __init__(self):
        self.t: float = 0.0
        self.ttl = 2000
        self.waves: list[Wave] = []
        self.traces: list[tuple[int, int, int],] = []

    def add_wave(self, wave: Wave):
        self.waves.append(wave)
        min_freq = min(self.waves, key=lambda w: w.freq).freq
        self.ttl = int((1000 / min_freq) * 0.95)

    def update(self, dt: float):
        self.t += dt

    def render(self, screen):
        self.traces = list(filter(lambda t: pg.time.get_ticks() - t[2] < self.ttl, self.traces))
        sum_x = 400.0
        sum_y = 300.0
        for wave in self.waves:
            sum_x, sum_y = wave.render(screen, self.t, sum_x, sum_y)
        self.traces.append((int(sum_x), int(sum_y), pg.time.get_ticks()))
        for trace in self.traces:
            pg.draw.circle(screen, WHITE, trace[:2], 1)
