from Character import Character

class Party(Character):
    def __init__(self, file_name):
        super().__init__(file_name, *self.get_information(file_name))

    def get_information(file_name):
        try:
            with file.open("Party/" + file_name + ".txt") as file:
                values = [file.nextline()]
                for value in file.nextline().split(" "):
                    values.append(int(value))
                return tuple(values)
        except ValueError:
            print(f"Error creating {file_name} party member")
            return ("MissingNo.", 0, 0, 0)
        except FileNotFoundError:
            print(f"Party/{file_name}.txt not found.")
            return ("MissingNo.", 0, 0, 0)