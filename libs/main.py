# main.py
# Main display class that updates and draws on Pygame instances
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *

from .button import Button
from .color import BLACK, WHITE
from .display import Display
from .memory import Memory


class main(object):
    """
    Display class that allows Pygame updating, rendering, and running
    """
    def __init__(self, width=300, height=400):
        pg.init()
        pg.display.set_caption("Calculator")
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.fps = 60
        self.clock = pg.time.Clock()
        self.running = True
        self.display = Display(x=self.WIDTH//2, y=0,
                               width=300, height=70)

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN and event.key == K_ESCAPE:
                self.running = False
        
    def update(self):
        self.display.update()

    def render(self):
        self.screen.fill(WHITE)
        self.display.render(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self.event_loop()
            self.update()
            self.render()
            self.clock.tick(self.fps)
        pg.quit()

    