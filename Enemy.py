from Character import Character
import random

class Enemy(Character):
    def __init__(self, file_name):
        super().__init__(file_name)

    # Attack is random for enemies, with a 1/3 chance of a special attack.
    # Special attacks do 1.5x the damage, but have limited uses.
    def attack(self):
        choice = random.randint(0, 2)
        print(self.get_damage())

        if choice == 2 and self.get_special > 0:
            self.change_special(-1)
            return self.get_damage() * 1.5
        else:
            return self.get_damage()


        
