from ItemClasses.Item import Item

class SelfItem(Item):
    def __init__(self, file_name, heal_amount):
        super().__init__(file_name, "Self")

        self.__heal_amount = heal_amount

    def get_heal(self):
        return self.__heal_amount