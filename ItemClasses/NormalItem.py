from ItemClasses.Item import Item

class NormalItem(Item):
    def __init__(self, file_name, damage_amount):
        super().__init__(file_name, "Normal")

        self.__damage_amount = damage_amount

    def get_damage(self):
        return self.__damage_amount