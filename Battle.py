import pygame
from Initializer import BattleInitializer
from Enemy import Enemy

# Class which creates a battle between the user's party and generated enemies
#
# Generates enemies at the start and loads the user's characters and party.
class Battle():
    def __init__(self):
        self.generate_enemies()
        pass

    def update(self):
        pass

    def draw(self, screen):
        self.__enemies.draw(screen)
        self.__party.draw(screen)
        self.__items.draw(screen)
    
    # Generates enemies randomly 
    def generate_enemies(self):
        self.__enemies = pygame.sprite.Group(BattleInitializer.create_enemies())

        items, party = BattleInitializer.create_party()
        self.__items = pygame.sprite.Group(items)
        self.__party = pygame.sprite.Group(party)

    def generate_user(self):
        pass