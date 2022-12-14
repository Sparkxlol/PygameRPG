import pygame
from ImageInformation import ImageInformation
import Initializer

# Class that inherits from the pygame Sprite class.
# 
# Allows creation of multiple frames of sprites based on one given image.
# This improves performance due to using one image, and allows animation.
#### Animation not yet created ####
class Spritesheet(pygame.sprite.Sprite):
    SCALE_FACTOR = Initializer.SCALE_FACTOR

    def __init__(self, file_name):
        super().__init__()
        self.__flipped = False

        try:
            self.frames = self.create_frames(file_name)
            self.set_frame(0)
        except Exception as e:
            # If the image could not be loaded an exception is thrown.
            print(f"Error loading {file_name}.png")
            raise

        self.rect = self.image.get_rect()
        self.__name = file_name


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
            frame = pygame.Surface(mask_size, pygame.SRCALPHA).convert_alpha()

            # Sets the sprite to the initial image in the sheet.
            # Takes the image, the initial location, and then a Rect of the top-left and size.
            frame.blit(img, (0, 0), ((x, y), mask_size))
            # Scales up and adds to the list.
            frames.append(pygame.transform.scale(frame,
                (frame.get_size()[0] * Spritesheet.SCALE_FACTOR, frame.get_size()[1] * Spritesheet.SCALE_FACTOR)))

            # Goes through each sprite on the x-axis until the end, then loops to the next row.
            x += mask_size[0]
            if x >= total_size[0]:
                y += mask_size[1]
                x = 0

        return frames

    def set_flip(self, flip):
        self.__flipped = flip
        self.set_frame(0)

    # Sets the sprite to the frame at the given index.
    def set_frame(self, index):
        if self.__flipped:
            self.image = pygame.transform.flip(self.frames[index], True, False)
        else:
            self.image = self.frames[index]

    # Sets the position of the sprite.
    def set_position(self, location):
        self.rect = pygame.Rect(location, (self.rect.width, self.rect.height))

    # Returns the position of the sprite.
    def get_position(self):
        return self.rect

    # Returns the dimensions of the sprite.
    def get_size(self):
        return self.rect.size

    def __str__(self):
        return f"{self.__name}: {self.get_position()}"

    def update(self):
        pass