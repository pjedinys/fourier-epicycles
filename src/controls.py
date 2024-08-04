import pygame
from src.fourier import calculate_cycles

class Controls:
    def __init__(self, window):
        self.window = window

    def paint(self, event, state):
        x, y = event.pos[0] - self.window.width / 2, event.pos[1] - self.window.height / 2
        state.x.append(x)
        state.y.append(y)

    def handle_events(self, state):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.window.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.window.resize(event.w, event.h)
                state.center = (self.window.width / 2, self.window.height / 2)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.window.start_drawing()
                state.reset()
                self.paint(event, state)
            elif event.type == pygame.MOUSEMOTION and self.window.drawing:
                self.paint(event, state)
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.window.stop_drawing()
                state.center = (self.window.width / 2, self.window.height / 2)
            elif event.type == pygame.MOUSEWHEEL:
                state.update_order(event.y)
                calculate_cycles(state)
