from Spritesheet import Spritesheet

# Class which the user's characters and the enemies are derived.
#
# Has health, damage, and special point variables.
class Character(Spritesheet):
    def __init__(self, file_name, name, health, damage, special):
        super().__init__(file_name)

        self.__name = name
        self.__initial_health = health
        self.__initial_special = special
        self.__damage = damage

        self.__health = health
        self.__special = special

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def get_special(self):
        return self.__special

    def get_total_health(self):
        return self.__initial_health
    
    def get_total_special(self):
        return self.__initial_special

    def get_damage(self):
        return self.__damage

    def change_health(self, amount = None):
        if amount == None:
            self.__health = self.get_total_health()
        else:
            if self.__health + amount > self.get_total_health():
                self.__health = self.get_total_health()
            else:
                self.__health += amount

    def change_special(self, amount = None):
        if amount == None:
            self.__special = self.get_total_special()
        else:
            self.__special += amount
    
    def __str__(self):
        return self.__name + " " + str(self.__health)