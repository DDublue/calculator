# memory.py
# Stores the memory of the calculator
# ---------------------------------------------------------------------

import pygame
from pygame.locals import *

class Memory(object):
    """
    Memory class that stores the information for the calculator.
    This includes the answer and a user-saved number.

    self.show: int = 0
    self.current: int = 0
    self.answer: float = 0
    self.cache: int = 0
    """
    def __init__(self):
        self._current = ""
        self._answer = ""
        self._cache = ""

    @property
    def current(self):
        return self._current
    
    @current.setter
    def current(self, val):
        self._current = val

    @property
    def answer(self):
        return self._answer
    
    @answer.setter
    def answer(self, ans):
        self._answer = ans
        
    @property
    def cache(self):
        return self._cache
    
    @cache.setter
    def cache(self, cache):
        self._cache = cache
        
    @cache.setter
    def cache_add(self, cache):
        self._cache += cache
        
    @cache.setter
    def cache_sub(self, cache):
        self._cache -= cache
    
    def clear_current(self):
        self._current = ""

    def clear_answer(self):
        self._answer = ""
        
    def clear_cache(self):
        self._cache = ""
        