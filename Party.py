from Character import Character

POWER_UP = False

class Party(Character):
    def __init__(self, file_name):
        super().__init__(file_name)

        self.__item = None
        self.set_flip(True)

        ####### TEMP CHANGE ########
        # Changes health and damage to make more fair, may change in the future.
        if POWER_UP:
            self.set_max_health(self.get_health() * 2)
            self.set_damage(self.get_damage() * 1.5)

    # Returns the amount of the damage the character should deal based on item.
    def get_damage(self):
        # Default damage.
        if self.__item == None or self.__item.get_type() == 'Heal':
            return super().get_damage()
        # Damage holding an attacking weapon.
        elif self.__item.get_type() == 'Normal':
            return super().get_damage() + self.__item.get_damage()
        # Damage holding a special weapon.
        else:
            special = self.__item.get_special()
            self.change_special(-special[1])
            return super().get_damage() + special[0]

    def set_item(self, item):
        self.__item = item
    
    def get_item(self):
        return self.__item