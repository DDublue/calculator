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
        self.memory = Memory()
        self.esc_down = False
        self.buttons = self._create_buttons()

    def _create_buttons(self):
        self.buttons = []
        chars = [
            'MC','MR','M-','M+',
            'C','S','%','/',
            '7','8','9','*',
            '4','5','6','-',
            '1','2','3','+',
            'E', '0','.','='
            ]
        for row in range(6):
            for col in range(4):
                b = Button(char=chars[row*4+col], x=row, y=col)
                print(b.char, end=' ')
                self.buttons.append(b)
            print()
        return self.buttons

    def _event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN and event.key == K_ESCAPE:
                self.esc_down = True

            if event.type == pg.KEYUP and event.key == K_ESCAPE and self.esc_down:
                self.esc_down = False
                self.running = False

    def _update(self):
        self.display.update(self.memory.answer)

    def _render(self):
        self.screen.fill(WHITE)
        self.display.render(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self._event_loop()
            self._update()
            self._render()
            self.clock.tick(self.fps)
        pg.quit()

    