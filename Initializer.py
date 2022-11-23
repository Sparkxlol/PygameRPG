import os
import random
from ItemClasses import *
from Enemy import Enemy

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

# Function used to create a random list of enemies.
def create_enemies():
    enemy_directories = os.listdir("./Enemies")
    enemies = []

    random_enemy = random.randint(0, len(enemy_directories) - 1)

    for i in range(random.randint(1, 3)):
        enemies.append(Enemy(enemy_directories[random_enemy].removesuffix(".txt")))
    
    return enemies
