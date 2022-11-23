import pygame
from Game import Game

def main():
    pygame.init()

    FPS = 60
    clock = pygame.time.Clock()

    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 1000

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game = Game()
    
    # Main game loop, until the user quits.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return # Breaks out of the function to stop the game.
        
        screen.fill((0, 0, 0))

        game.update()
        game.draw(screen)

        pygame.display.update()

        clock.tick(FPS)


# Calls main if program is run from this file.
if __name__ == "__main__":
    main()