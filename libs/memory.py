# memory.py
# Stores the memory of the calculator
# ---------------------------------------------------------------------

import pygame
from pygame.locals import *

class Memory(object):
    """
    Memory class that stores the information for the calculator.
    
    This includes the answer and a user-saved number.
    """
    def __init__(self):
        self.answer = 0
        self.cache = 0
        
    def get_answer(self):
        return self.answer
    
    def get_cache(self):
        return self.cachce
    
    def set_answer(self, ans):
        self.answer = ans
        
    def set_cache(self, cache):
        self.cache = cache
        
    def set_cache_add(self, cache):
        self.cache += cache
        
    def set_cache_sub(self, cache):
        self.cache -= cache
        
    def clear_answer(self):
        self.answer = 0
        
    def clear_cache(self):
        self.cache = 0
        