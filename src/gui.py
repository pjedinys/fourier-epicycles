import pygame

WIDTH = 800
HEIGHT = 600
SPEED = 0.1

pygame.init()
pygame.display.set_caption("")

class Window:
    def __init__(self, width=WIDTH, height=HEIGHT):
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.width = width
        self.height = height
        self.running = True
        self.drawing = False
        self.time = 0

    def resize(self, width, height):
        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

    def start_drawing(self):
        self.drawing = True
        self.time = 0

    def stop_drawing(self):
        self.drawing = False
