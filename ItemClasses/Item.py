from Spritesheet import Spritesheet

# Class which inherits from the spritesheet.
#
# Used to define what an stats an item has.
# Three types of items: healing / self, default attacking, special attacking.
#
# Template for item files:
# type of item - self, normal, special
# values - self: heal amount, normal: attack damage, special: attack damage and sp usage 
class Item(Spritesheet):
    def __init__(self, file_name):
        super().__init__(file_name)

        self.read_file(file_name)
        self.__type = None
    
    def get_type(self):
        return self.__type

    def update(self):
        pass