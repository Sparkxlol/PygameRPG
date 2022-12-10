import pygame

# Initializes pygame and pygame's font.
pygame.init()
pygame.font.init()

import Initializer
from Game import Game

def main():
    clock = pygame.time.Clock()

    # Sets up display, window, and icon.
    screen = pygame.display.set_mode((Initializer.SCREEN_WIDTH, Initializer.SCREEN_HEIGHT))
    pygame.display.set_caption("Mysteria")

    icon = pygame.image.load("Images/icon.png")
    pygame.display.set_icon(icon)

    game = Game()
    
    # This loop continues through the whole game, and updates the 
    # game object which updates every other object in the program.
    while True:
        screen.fill((0, 0, 0))

        game.update()
        game.draw(screen)

        pygame.display.update()

        # Runs at the FPS set in the Initializer class.
        clock.tick(Initializer.FPS)
    
# Calls main if program is run from this file.
if __name__ == "__main__":
    main()