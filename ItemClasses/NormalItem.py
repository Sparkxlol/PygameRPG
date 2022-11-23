from Item import Item

class NormalItem(Item):
    def __init__(self, file_name, damage_amount):
        super().__init__(file_name)

        self.__damage_amount = damage_amount

    def use_item(self, character):
        pass