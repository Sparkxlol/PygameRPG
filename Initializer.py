SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
SCALE_FACTOR = 10

import os
import random
from ItemClasses import *
from Spritesheet import Spritesheet
from Enemy import Enemy
from Party import Party

# Function used to create items based on the given text file.
def create_item(file_name):
    try:
        with open("Items/" + file_name + ".txt", "r") as file:
            item_type = file.readline().strip()

            # Match statement to check what type of item it is, and
            # create the corresponding item with the stats given.
            match item_type:
                case "self":
                    heal_amount = int(file.readline())
                    return SelfItem.SelfItem(file_name, heal_amount)
                case "normal":
                    damage_amount = int(file.readline())
                    return NormalItem.NormalItem(file_name, damage_amount)
                case "special":
                    stats = file.readline().split(" ")
                    return SpecialItem.SpecialItem(file_name, int(stats[0]), int(stats[1]))
                case other:
                    raise ValueError
    except ValueError:
        # Prints a ValueError if any values are improperly formatted.
        print(f"Items/{file_name}.txt improperly formatted")
        raise
    except FileNotFoundError:
        print(f"Items/{file_name}.txt could not be found")
        raise

class BattleInitializer():
    # Function used to create a random list of enemies.
    def create_enemies():
        try:
            enemy_directories = os.listdir("./Characters")
            enemies = []

            for i in range(random.randint(1, 3)):
                random_enemy = random.randint(0, len(enemy_directories) - 1)
                enemies.append(Enemy(enemy_directories[random_enemy].removesuffix(".txt")))
            
            return enemies
        except OSError:
            print("Characters file could not be accessed.")
            raise
    
    # Creates the user's items and characters.
    # Reads from the corresponding user.txt file.
    #
    # Returns a tuple of items and party members.
    #
    # File formatted as:
    # List of item names,   which are loaded from their corresponding files.
    # 
    # Name of user's character          (Repeated 3 lines for each party member)
    # Name of the character in file,    which is then loaded from the corresponding file.
    # Equipped item,    which is found in the item list and set to the character.
    def create_party():
        try:
            with open("user.txt", "r") as file:
                item_names = file.readline().strip().split(" ")
                items = [create_item(item) for item in item_names]
                characters = []

                while file.readline() == '\n':
                    name = file.readline().strip()
                    character = Party(file.readline().strip())
                    character.set_name(name)
                    
                    held_item = file.readline().strip()
                    
                    # Sets the party member's item to the given item if it's not already equipped and exists.
                    if held_item in item_names and not items[item_names.index(held_item)].get_equipped:
                        character.set_item(items[item_names.index(held_item)])
                        items[item_names.index(held_item)].set_equipped = True
                    else:
                        character.set_item(None)

                    characters.append(character)
            
            return (items, characters)
        except Exception:
            print("User.txt file couldn't be read")
            raise
    
    # Returns a random background from Images/Backgrounds.
    # Used by the UI to make the background during Battle mode.
    def create_background():
        try:
            backgrounds = os.listdir("./Images/Backgrounds")
            background_choice = random.randint(0, len(backgrounds) - 1)

            return Spritesheet("Backgrounds/" + backgrounds[background_choice].removesuffix(".png"))
        except Exception:
            print("Background couldn't be accessed.")
            raise

