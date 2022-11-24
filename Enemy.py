from Character import Character
import random

# Class which inherits from character.
#
# Used to define an enemy with basic stats.
#
# Template for enemy files:
# Name
# Health, Damage, Special
class Enemy(Character):
    def __init__(self, file_name):
        super().__init__(file_name, *Enemy.get_information(file_name))
    
    def get_information(file_name):
        try:
            with open("Enemies/" + file_name + ".txt") as file:
                values = [file.readline().strip()]
                for value in file.readline().split(" "):
                    values.append(int(value))
                return tuple(values)
        except ValueError:
            print(f"Error creating {file_name} enemy")
            return ("MissingNo.", 0, 0, 0)
        except FileNotFoundError:
            print(f"Enemies/{file_name}.txt not found.")
            return ("MissingNo.", 0, 0, 0)

    # Attack is random for enemies, with a 1/3 chance of a special attack.
    # Special attacks do 1.5x the damage, but have limited uses.
    def attack(self):
        choice = random.randint(0, 2)

        if choice == 2 and self.get_special > 0:
            self.change_special(-1)
            return self.get_damage() * 1.5
        else:
            return self.get_damage()


        
