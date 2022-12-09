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

    # Returns the name of the character.
    def get_name(self):
        return self.__name

    # Sets the name to the given name.
    def set_name(self, name):
        self.__name = name

    # Returns the current healht of the character.
    def get_health(self):
        return self.__health

    # Returns the current amount of special points remaining.
    def get_special(self):
        return self.__special

    # Returns the max health the character has.
    def get_total_health(self):
        return self.__initial_health
    
    # Returns the total special points the character has.
    def get_total_special(self):
        return self.__initial_special

    # Returns the damage the character deals.
    def get_damage(self):
        return self.__damage
    
    # Changes the current health of the enemy, but sets limit on max and min health.
    # If nothing is inputted, the health is changed to max.
    def change_health(self, amount = None):
        if amount == None:
            self.__health = self.get_total_health()
        else:
            if self.__health + amount > self.get_total_health():
                self.__health = self.get_total_health()
            else:
                self.__health += amount

    # Changes the amount of special based on user input.
    # If nothing is inputted, the health is changed to max.
    def change_special(self, amount = None):
        if amount == None:
            self.__special = self.get_total_special()
        else:
            self.__special += amount
    
    # Prints out the characters name and current health.
    def __str__(self):
        return self.__name + " " + str(self.__health)