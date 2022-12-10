from ItemClasses.Item import Item

# Class which inherits from Item and affects default damage.
class NormalItem(Item):
    def __init__(self, file_name, damage_amount):
        super().__init__(file_name, "Normal")

        self.__damage_amount = damage_amount

    # Returns the amount of damage this item does.
    def get_damage(self):
        return self.__damage_amount