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

    # Placeholder function to be overrided in each subclass.
    def use_item(self, character):
        pass

    def update(self):
        pass
    
    # Static method used to create items based on the given text file.
    def create_item(file_name):
        try:
            with open("Items/" + file_name + ".txt") as file:
                item_type = file.readline()

                match item_type:
                    case "self":
                        pass
                    case "normal":
                        pass
                    case "special":
                        pass
                    case other:
                        raise ValueError
        except ValueError:
            # Prints a ValueError if any values are improperly formatted.
            print(f"Items/{file_name}.txt improperly formatted")
            raise
        except FileNotFoundError:
            print(f"Items/{file_name}.txt could not be found")
            raise