import pygame
import random
import Initializer
from Initializer import BattleInitializer
from UI import BattleUI

# Class which creates a battle between the user's party and generated enemies
#
# Generates enemies at the start and loads the user's characters and party.
# Holds three groups in a dictionary (Enemies, Party, Items)
class Battle():
    def __init__(self):
        self.generate_game()
        self.move_locations(self.__groups["Enemies"], "Enemies")
        self.move_locations(self.__groups["Party"], "Party")
        self.__UI = BattleUI(self.__groups)
        self.__ended = False

    def update(self):
        self.__UI.update()

        # Checks if the user has chosen a mode as well as a target.
        targets = self.__UI.get_targets()
        
        # Allows options for each party member, and then the enemies.
        if targets != None:
            self.user_attack(targets)

            if not self.__ended:
                self.__UI.set_party(self.__UI.get_party() + 1)

                if self.__UI.get_party() == len(self.__groups["Party"]):
                    self.enemy_attack()
                    self.__UI.set_party(0)
                
                # Resets positions after someone attacks.
                self.__UI.reset()
    
    def end(self):
        return self.__ended or self.__UI.get_mode == "Exit"

    # Draws the UI along with all alive characters.
    def draw(self, screen):
        self.__UI.draw(screen)
        self.__groups["Enemies"].draw(screen)
        self.__groups["Party"].draw(screen)
    
    # Generates enemies randomly and reads items/party from user file using BattleInitalizer.
    def generate_game(self):
        self.__groups = {}
        self.__groups["Enemies"] = pygame.sprite.Group(BattleInitializer.create_enemies())

        items, party = BattleInitializer.create_party()
        self.__groups["Items"] = pygame.sprite.Group(items)
        self.__groups["Party"] = pygame.sprite.Group(party)
    
    # Moves the corresponding group into their correct position.
    # Uses the passed group_name to decide which side to position the group.
    def move_locations(self, group, group_name):
        # Spreads out each member evenly vertically.
        jump = (Initializer.SCREEN_HEIGHT - 200) / len(group) 
        pos_x = Initializer.SCREEN_WIDTH / 4 if group_name == "Party" else Initializer.SCREEN_HEIGHT / 4 * 3
        pos_y = jump / 2

        for sprite in group:
            sprite.set_position((pos_x - sprite.get_size()[0] / 2, pos_y - sprite.get_size()[1] / 2))
            pos_y += jump
    
    def check_UI(self):
        mode = self.__UI.get_mode()

        match mode:
            case 'Attack':
                pass
    
    def user_attack(self, target):
        mode = self.__UI.get_mode()
        group_name = "Enemies" if mode == "Attack" or mode == "Special" else "Party"
        party_member = self.__groups["Party"].sprites()[self.__UI.get_party()]
        
        match mode:
            case "Attack":
                target.change_health(-party_member.get_damage())
            case "Special":
                # Need to add decreasing special amount.
                target.change_health(-party_member.get_damage() * 1.5)
            case "Item":
                self.use_item(target)
                target = target[0]
        
        if target.get_health() <= 0:
            self.__groups[group_name].remove(target)
            if len(self.__groups[group_name]) > 0:
                self.move_locations(self.__groups[group_name], group_name)
            else:
                self.__ended = True
                self.__UI.set_move(False)
        
        print(target, mode)

    def enemy_attack(self):
        party = self.__groups["Party"]
        killed = False

        for enemy in self.__groups["Enemies"]:
            random_party = party.sprites()[random.randint(0, len(party) - 1)]

            random_party.change_health(-enemy.get_damage())
            print(random_party, "Attack")

            if random_party.get_health() <= 0:
                self.__groups["Party"].remove(random_party)
                killed = True
                
                if (len(party) <= 0):
                    self.__UI.set_move(False)
                    self.__ended = True
                    break
                    
        if killed and len(party) > 0:
            self.move_locations(self.__groups["Party"], "Party")

    # Passes a tuple holding the targets, with the last index being the item.
    # Can be using a Normal (Attacking), Self (Healing), or Special item.
    def use_item(self, target):
        item = target[-1]
        target = target[0]

        if item.get_type() == "Self":
            target.change_health(item.get_heal())
            item.kill()
        else:
            # Removes the item from any party members.
            if item.get_equipped:
                for party in self.__groups["Party"].sprites():
                    if party.get_item() is item:
                        party.set_item(None)
                        break

            target.set_item(item)
            item.set_equipped = True