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
    def __init__(self, file_name, given_type):
        super().__init__(file_name)

        self.__item_name = file_name
        self.__type = given_type
        self.__equipped = False
    
    def get_type(self):
        return self.__type
    
    def get_item_name(self):
        return self.__item_name

    def get_equipped(self):
        return self.__equipped
    
    def set_equipped(self, equipped):
        self.__equipped = equipped

    def update(self):
        pass