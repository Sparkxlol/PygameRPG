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

        self.__item_name = file_name
        self.__equipped = False

    # Placeholder function to be overrided in each subclass.
    def use_item(self, character):
        pass

    def get_item_name(self):
        return self.__item_name

    def set_equipped(self, equipped):
        self.__equipped = equipped
    
    def get_equipped(self):
        return self.__equipped

    def update(self):
        pass