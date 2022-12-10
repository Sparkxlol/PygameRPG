from Character import Character

# Makes easier battles.
POWER_UP = False

# Class which inherits off Character and defines an enemy
class Party(Character):
    def __init__(self, file_name):
        super().__init__(file_name)

        self.__item = None
        self.set_flip(True) # Flips sprite correct direction.

        ####### TEMP CHANGE ########
        # Changes health and damage to make fights easier if necessary, may remove in the future.
        if POWER_UP:
            self.set_max_health(self.get_health() * 2)
            self.set_damage(self.get_damage() * 1.5)

    # Returns the amount of the damage the character should deal based on item.
    def get_damage(self, type):
        # Damage holding an attacking weapon and attacking.
        if self.__item != None and self.__item.get_type() == 'Normal' and type == "Attack":
            return super().get_damage() + self.__item.get_damage()
        # Damage holding a special weapon and special attacking.
        elif self.__item != None and self.__item.get_type() == "Special" and type == "Special":
            special = self.__item.get_special()
            self.change_special(-special[1])
            return super().get_damage() + special[0]
        # Default damage.
        else:
            return super().get_damage()

    # Sets the held item.
    def set_item(self, item):
        self.__item = item
    
    # Returns the held item.
    def get_item(self):
        return self.__item