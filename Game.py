import sys
import pygame
from enum import Enum
from Battle import Battle

# Enum to help make the modes clearer.
class Mode(Enum):
    MENU = 1
    BATTLE = 2
    EXPLORE = 3

# Class designed to run the entire game.
#
# Has three modes using classes which change the "scene" of the game
# Main(), Battle() and Explore() classes are created depending on how the game changes.
# Each mode's UI is where events are iterated through, allowing easy access to player input.
class Game():
    def __init__(self):
        self.set_mode(Mode.BATTLE)

    def update(self):
        self.__mode.update()
        if self.check_end():
            self.set_mode(Mode.MENU)

    def draw(self, screen):
        self.__mode.draw(screen)
    
    def check_end(self):
        return self.__mode.end()

    # Each mode MUST have a draw, update and end method to work properly.
    # This function creates a new "mode" being the main menu, battle mode or explore mode.
    # This is similar to loading a new scene, since all sprites are destroyed and new ones are created.
    def set_mode(self, mode):
        match mode:
            case Mode.MENU:
                sys.exit()
            case Mode.BATTLE:
                self.__mode = Battle()
            case Mode.EXPLORE:
                pass

