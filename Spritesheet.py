import pygame
from ImageInformation import ImageInformation

class Spritesheet(pygame.sprite.Sprite):
    def __init__(self, file_name):
        super().__init__()

        try:
            self.image = pygame.image.load("Images/" + file_name + ".png").convert()
        except:
            print(f"Error loading {file_name}.png")
            self.image = pygame.image.load("Images/template.png").convert()

        self.img_info = ImageInformation(file_name)

        self.rect = self.image.get_rect()
    
    def set_sprite(self, index):
        self.rect = self.img_info.get_mask_size()

    def update(self):
        pass