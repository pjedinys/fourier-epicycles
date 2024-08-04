from numpy.fft import fft, ifft, fftfreq
import numpy as np
from src.gui import SPEED

class State:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = []
        self.y = []
        self.x_ifft = []
        self.y_ifft = []
        self.order = 0
        self.amps = [[], [], []]
        self.vels = []
        self.phases = [[], [], []]
        self.inds = [[], [], []]
        self.center = []

    def update_order(self, delta):
        self.order = max(0, self.order + delta)

def calculate_cycles(state):
    if not state.x:
        return

    x_fft = fft(state.x)
    y_fft = fft(state.y)
    n = state.order

    x_fft[n + 1: -n] = 0
    y_fft[n + 1: -n] = 0

    state.x_ifft = ifft(x_fft).real
    state.y_ifft = ifft(y_fft).real

    combined = x_fft + 1j * y_fft
    length = len(combined)

    state.amps[0] = np.abs(combined) / length
    state.vels = SPEED * 2 * np.pi * fftfreq(length)
    state.phases[0] = np.angle(combined)
    state.inds[0] = np.argsort(state.amps[0])[::-1]

    state.amps[1] = np.abs(x_fft) / length
    state.phases[1] = np.angle(x_fft)
    state.inds[1] = np.argsort(state.amps[1])[::-1]

    state.amps[2] = np.abs(y_fft) / length
    state.phases[2] = np.angle(y_fft)
    state.inds[2] = np.argsort(state.amps[2])[::-1]
