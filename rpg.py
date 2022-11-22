import pygame
from Spritesheet import Spritesheet

def main():
    pygame.init()

    FPS = 60
    clock = pygame.time.Clock()

    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    all_sprites = pygame.sprite.Group() # Holds all objects in the game.
    sword = Spritesheet("sword")

    all_sprites.add(sword)
    
    # Main game loop, until the user quits.
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return # Breaks out of the function to stop the game.
        
        all_sprites.update()

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.update()

        clock.tick(FPS)


# Calls main if program is run from this file.
if __name__ == "__main__":
    main()