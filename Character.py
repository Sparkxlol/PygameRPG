from Spritesheet import Spritesheet


# Class to create party members and enemies.
#
# Used to define an character with basic stats.
#
# Template for character files:
# Name
# Health, Damage, Special
class Character(Spritesheet):
    def __init__(self, file_name):
        super().__init__(file_name)

        information = Character.get_information(file_name)

        self.__name = information[0]
        self.__initial_health = information[1]
        self.__initial_special = information[2]
        self.__damage = information[3]

        self.__health = self.__initial_health
        self.__special = self.__initial_special

    def get_information(file_name):
        try:
            with open("Characters/" + file_name + ".txt") as file:
                values = [file.readline().strip()]
                for value in file.readline().split(" "):
                    values.append(int(value))
                return tuple(values)
        except ValueError:
            print(f"Error creating {file_name} party member")
            return ("MissingNo.", 0, 0, 0)
        except FileNotFoundError:
            print(f"Characters/{file_name}.txt not found.")
            return ("MissingNo.", 0, 0, 0)

    # Returns the name of the character.
    def get_name(self):
        return self.__name

    # Sets the name to the given name.
    def set_name(self, name):
        self.__name = name

    # Returns the current healht of the character.
    def get_health(self):
        return self.__health
    
    # Changes the max health of the character.
    def set_max_health(self, health):
        self.__initial_health = health
        self.__health = health

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

    # Changes the max damage of the character.
    def set_damage(self, damage):
        self.__damage = damage
    
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