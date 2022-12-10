from ItemClasses.Item import Item

# Class which inherits from Item and heals a party member.
class SelfItem(Item):
    def __init__(self, file_name, heal_amount):
        super().__init__(file_name, "Self")

        self.__heal_amount = heal_amount

    # Returns the heal amount for this item.
    def get_heal(self):
        return self.__heal_amount