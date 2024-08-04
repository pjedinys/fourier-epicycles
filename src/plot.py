import pygame
import numpy as np
from src.fourier import calculate_cycles

class Plot:
    def __init__(self, window):
        self.window = window

    def draw_path(self, x, y, color="white"):
        length = len(x)
        for i in range(length - 1):
            x1, y1 = x[i] + self.window.width / 2, y[i] + self.window.height / 2
            x2, y2 = x[i + 1] + self.window.width / 2, y[i + 1] + self.window.height / 2
            pygame.draw.line(self.window.screen, color, (x1, y1), (x2, y2), 1)

    def draw_chain(self, amp, ind, vel, phase, t, center, color="white", rot=False):
        cx, cy = center
        for i in ind:
            prev_cx, prev_cy = cx, cy
            cx += amp[i] * (np.sin if rot else np.cos)(vel[i] * t + phase[i])
            cy += amp[i] * (np.cos if rot else np.sin)(vel[i] * t + phase[i])
            pygame.draw.line(self.window.screen, color, (prev_cx, prev_cy), (cx, cy), 1)
            pygame.draw.circle(self.window.screen, color, (int(prev_cx), int(prev_cy)), int(amp[i]), 1)
        return cx, cy

    def draw_epicycles(self, t, state):
        calculate_cycles(state)
        x1, y1 = self.draw_chain(state.amps[1], state.inds[1], state.vels, state.phases[1], t, state.center, (64, 64, 64))
        x2, y2 = self.draw_chain(state.amps[2], state.inds[2], state.vels, state.phases[2], t, state.center, (64, 64, 64), rot=True)
        pygame.draw.rect(self.window.screen, (128, 128, 128), pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2)), 1)
        self.draw_chain(state.amps[0], state.inds[0], state.vels, state.phases[0], t, state.center, "white")
