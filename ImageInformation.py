# Class used to process and access spritesheet information
class ImageInformation():
    def __init__(self, file_name):
        self.read_file(file_name)
    
    def read_file(self, file_name):
        try:
            with open(file_name + ".txt", 'r') as file:
                self.total_size = tuple(file.next())
                self.mask_size = tuple(file.next())
                self.sprite_count = file.next() 
        except:
            print(f"Error loading {file_name}.txt")
            self.total_size = (0, 0)
            self.mask_size = (0, 0)
            self.sprite_count = 0
    
    def get_total_size(self):
        return self.total_size
    
    def get_mask_size(self):
        return self.mask_size

    def get_sprite_count(self):
        return self.sprite_count