# button.py
# Button GUI
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from .color import BLACK, LGRAY2, GRAY2, WHITE


class Button(object):
    """
    Button GUI
    """
    def __init__(self, char, x, y, width=75, height=55):
        self.surf = pg.Surface((width, height))
        self.surf_rect = self.surf.get_rect(topleft=(x,y))
        self._char = char
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.main_color = WHITE
        self.hover_color = LGRAY2
        self.click_color = GRAY2
        self.current_color = self.main_color
        self.font = pg.font.Font("./data/font/PocketCalculator.ttf", 30)
        self.text = self.font.render(self._char, True, BLACK)
        self.text_rect = self.text.get_rect(center=(width//2, height//2))
        self.hovering = False
        self.button_held = False
        self.mb1 = False
    
    def update(self): # update button color when idle, hover, and click
        self.button_hover()
        if self.button_held:
            self.current_color = self.click_color
        elif self.hovering and not self.mb1:
            self.current_color = self.hover_color
        else:
            self.current_color = self.main_color
    
    def render(self, screen):
        screen.blit(self.surf, self.surf_rect)
        self.surf.fill(self.current_color)
        self.surf.blit(self.text, self.text_rect)

    @property
    def char(self):
        return self._char

    def button_hover(self):
        if self.surf_rect.collidepoint(pg.mouse.get_pos()):
            self.hovering = True
        else:
            self.hovering = False

    def button_pressed(self):
        if self.pressed:
            self.pressed = False
            return True
        else:
            return False
                        
    def get_event(self, event): # fix
        # detects if a button is pressed and held properly
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.mb1 = True
            if self.surf_rect.collidepoint(event.pos):
                print(f"[CHAR: {self._char}] button down!")
                self.current_color = self.click_color
                self.button_held = True
        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.mb1 = False
            if self.surf_rect.collidepoint(event.pos) and self.button_held:
                print(f"[CHAR: {self._char}] button up!")
                self.current_color = self.main_color
                self.pressed = True
            else:
                self.current_color = self.main_color
            self.button_held = False