import pygame

pygame.init()
pygame.font.init()

import Initializer
from Game import Game

def main():
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((Initializer.SCREEN_WIDTH, Initializer.SCREEN_HEIGHT))
    pygame.display.set_caption("Mysteria")

    icon = pygame.image.load("Images/icon.png")
    pygame.display.set_icon(icon)

    game = Game()
    
    # Main game loop, until the user quits.
    while True:
        screen.fill((0, 0, 0))

        game.update()
        game.draw(screen)

        pygame.display.update()

        clock.tick(Initializer.FPS)

# Calls main if program is run from this file.
if __name__ == "__main__":
    main()



    