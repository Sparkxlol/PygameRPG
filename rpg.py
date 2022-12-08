import pygame
import Initializer
from Game import Game

def main():
    pygame.init()

    FPS = 60
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((Initializer.SCREEN_WIDTH, Initializer.SCREEN_HEIGHT))

    game = Game()
    
    # Main game loop, until the user quits.
    while True:
        screen.fill((0, 0, 0))

        game.update()
        game.draw(screen)

        pygame.display.update()

        clock.tick(FPS)


# Calls main if program is run from this file.
if __name__ == "__main__":
    main()



    