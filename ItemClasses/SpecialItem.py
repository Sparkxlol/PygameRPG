from ItemClasses.Item import Item

# Class which inherits from Item and affects special damage.
class SpecialItem(Item):
    def __init__(self, file_name, damage_amount, special_amount):
        super().__init__(file_name, "Special")

        self.__damage_amount = damage_amount
        self.__special_amount = special_amount

    # Returns a tuple of the special damage and special usage.
    def get_special(self):
        return (self.__damage_amount, self.__special_amount)