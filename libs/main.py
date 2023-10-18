# main.py
# Main display class that updates and draws on Pygame instances
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from libs.color import BLACK, WHITE

class main(object):
    """
    Display class that allows Pygame updating, rendering, and running
    """
    def __init__(self, width=300, height=400):
        pg.init()
        pg.display.set_caption("Calculator")
        self.WIDTH = width
        self.HEIGHT = height
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.RESIZABLE)
        self.fps = 60
        self.clock = pg.time.Clock()
        self.running = True

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
        
    def logic(self):
        pass

    def render(self, screen):
        self.screen.fill(WHITE)
        pg.display.update()

    def run(self):
        while self.running:
            self.event_loop()
            self.logic()
            self.render(self.screen)
            self.clock.tick(self.fps)
        pg.quit()

    