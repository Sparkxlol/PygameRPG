from Character import Character

class Party(Character):
    def __init__(self, file_name):
        super().__init__(file_name, *Party.get_information(file_name))

        self.__item = None

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

    def get_information(file_name):
        try:
            with open("Party/" + file_name + ".txt") as file:
                values = [file.readline()]
                for value in file.readline().split(" "):
                    values.append(int(value))
                return tuple(values)
        except ValueError:
            print(f"Error creating {file_name} party member")
            return ("MissingNo.", 0, 0, 0)
        except FileNotFoundError:
            print(f"Party/{file_name}.txt not found.")
            return ("MissingNo.", 0, 0, 0)