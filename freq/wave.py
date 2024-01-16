import math

import pygame as pg

from freq.colors import GRAY


class Wave:
    def __init__(self, freq: float, ampl: float, phase: float):
        self.freq = freq
        self.ampl = ampl
        self.phase = phase

    def __repr__(self):
        return f"Wave(freq={self.freq}, ampl={self.ampl}, phase={self.phase})"

    def render(
        self, screen, t: float, x, y, render_circle=True, render_line=True
    ) -> tuple[float, float]:
        w_x = self.ampl * math.cos(2 * math.pi * self.freq * t + self.phase)
        w_y = self.ampl * math.sin(2 * math.pi * self.freq * t + self.phase)
        if render_line:
            pg.draw.line(screen, GRAY, (x, y), (x + w_x, y + w_y), 1)
        if render_circle:
            pg.draw.circle(screen, GRAY, (x, y), self.ampl, 1)
        return (x + w_x, y + w_y)
