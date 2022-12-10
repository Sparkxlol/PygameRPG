from Item import Item

class SpecialItem(Item):
    def __init__(self, file_name, damage_amount, special_amount):
        super().__init__(file_name)

        self.__damage_amount = damage_amount
        self.__special_amount = special_amount
        self.__type = "Special"

    def get_special(self):
        return (self.__damage_amount, self.__special_amount)