import pygame
from ImageInformation import ImageInformation

# Class that inherits from the pygame Sprite class.
# 
# Allows creation of multiple frames of sprites based on one given image.
# This improves performance due to using one image, and allows animation.
class Spritesheet(pygame.sprite.Sprite):
    def __init__(self, file_name):
        super().__init__()

        try:
            self.frames = self.create_frames(file_name)
            self.set_frame(3)
        except Exception:
            # If the image could not be loaded a template image is loaded.
            # Program will most likely break either way due to animations.
            print(f"Error loading {file_name}.png")
            self.image = pygame.image.load("Images/template.png").convert()

        self.rect = self.image.get_rect()


    # Creates a list of Surfaces with each image from the given file.
    # Uses an ImageInformation object to get data about the given image.
    def create_frames(self, file_name):
        img_info = ImageInformation(file_name)
        img = pygame.image.load("Images/" + file_name + ".png").convert_alpha()
        frames = []

        mask_size = img_info.get_mask_size()
        total_size = img_info.get_total_size()

        x = 0
        y = 0

        for i in range(img_info.get_sprite_count()):
            frame = pygame.Surface(mask_size).convert_alpha()

            # Sets the sprite to the initial image in the sheet.
            # Takes the image, the initial location, and then a Rect of the top-left and size.
            frame.blit(img, (0, 0), ((x, y), mask_size))
            frames.append(frame)

            # Goes through each sprite on the x-axis until the end, then loops to the next row.
            x += mask_size[0]
            if x >= total_size[0]:
                y += mask_size[1]
                x = 0

        return frames

    # Sets the sprite to the frame at the given index.
    def set_frame(self, index):
        self.image = self.frames[index]

    def update(self):
        pass