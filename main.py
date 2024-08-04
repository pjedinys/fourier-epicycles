import pygame
from src.controls import Controls
from src.gui import Window, SPEED
from src.plot import Plot
from src.fourier import State

def main():
    window = Window()
    controls = Controls(window)
    plot = Plot(window)
    state = State()

    while window.running:
        window.screen.fill((0, 0, 0))
        plot.draw_path(state.x, state.y, "dark gray")

        if not window.drawing and state.x:
            window.time += 1 
            plot.draw_epicycles(window.time, state)
            length = len(state.x_ifft)
            plot.draw_path(state.x_ifft[:int(SPEED * window.time) % length + 1], 
                           state.y_ifft[:int(SPEED * window.time) % length + 1])

        controls.handle_events(state)
        pygame.display.flip()
        window.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
