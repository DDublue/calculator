# button.py
# Button GUI
# ---------------------------------------------------------------------

import pygame as pg
from pygame.locals import *
from .color import BLACK, LGRAY1, LGRAY2, DGRAY1, WHITE


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
        self.click_color = DGRAY1
        self.current_color = self.main_color
        self.font = pg.font.Font("./data/font/PocketCalculator.ttf", 30)
        self.text = self.font.render(self._char, True, BLACK)
        self.text_rect = self.text.get_rect(center=(width//2, height//2))
        self.hovering = False
        self.button_down = False
        self.button_up = True
    
    def update(self): # update button color when idle, hover, and click
        self.button_hover()
        if self.hovering:
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

    def button_hover(self): # fix
        if self.surf_rect.collidepoint(pg.mouse.get_pos()):
            self.hovering = True
        else:
            self.hovering = False

    def button_pressed(self): # fix
        if self.button_down:
            self.button_up = False
            
            
        
                
    def get_event(self, event): # fix
        if self.hovering:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.button_down = True
                self.button_up = False
            else:
                self.button_down = False
                self.button_up = True
        