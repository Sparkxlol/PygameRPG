from Item import Item

class SelfItem(Item):
    def __init__(self, file_name, heal_amount):
        super().__init__(file_name)

        self.__heal_amount = heal_amount

    def use_item(self, character):
        pass