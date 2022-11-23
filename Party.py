from Character import Character

class Party(Character):
    def __init__(self, file_name):
        super().__init__(file_name, *Party.get_information(file_name))

        self.__item = None

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