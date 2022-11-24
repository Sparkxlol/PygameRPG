# Class used to process and access spritesheet information
#
# MakeFile.py can be used to create ImageInformation files when given an image.
#
# File at ImageInformation/file_name.txt formatted as:
# total_x, total_y
# single_x, single_y
# frame_count
class ImageInformation():
    def __init__(self, file_name):
        self.read_file(file_name)
    
    # Attempts to access the given file and parse information out.
    # Saves the total image size, the size of each frame, and the total count of frames.
    def read_file(self, file_name):
        try:
            with open("ImageInformation/" + file_name + ".txt", 'r') as file:
                self.total_size = tuple([int(i) for i in file.readline().split(" ")])
                self.mask_size = tuple([int(i) for i in file.readline().split(" ")])
                self.sprite_count = int(file.readline()) 
        except FileExistsError:
            # If the file cannot be parsed, each of the values are set to 0.
            print(f"Error loading {file_name}.txt")
            self.total_size = (0, 0)
            self.mask_size = (0, 0)
            self.sprite_count = 0
    
    # Returns the images total size.
    def get_total_size(self):
        return self.total_size
    
    # Returns each tile's size.
    def get_mask_size(self):
        return self.mask_size

    # Returns the amount of tiles in the image.
    def get_sprite_count(self):
        return self.sprite_count