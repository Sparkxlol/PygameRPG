from Item import Item

class SelfItem(Item):
    def __init__(self, file_name, heal_amount):
        super().__init__(file_name)

        self.__heal_amount = heal_amount
        self.__type = "Self"

    def get_heal(self):
        return self.__heal_amount