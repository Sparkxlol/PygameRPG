import sys
import pygame
import Initializer
from Initializer import BattleInitializer
from Spritesheet import Spritesheet

class BattleUI():
    def __init__(self, groups):
        # UI Materials: Background, Buttons, etc.
        self.__background = BattleInitializer.create_background()
        self.__user_options = Spritesheet("battleUI")
        self.__user_options.set_position((0, Initializer.SCREEN_HEIGHT - Initializer.SCALE_FACTOR * 20))
        self.__user_option_index = 0
        self.__user_option_chosen = Spritesheet("battleUIChosen")
        self.move_chooser("None")

        # Groups to draw sprites
        self.__drawn_sprites = pygame.sprite.Group()
        self.__drawn_sprites.add(self.__background)
        self.__drawn_sprites.add(self.__user_options)
        self.__drawn_sprites.add(self.__user_option_chosen)

        # Mode information: None, Attack, Special, Item, Exit
        self.__groups = groups # All enemy, party, and item sprites, needed to check positions
        self.__mode = None 
        self.__mode_chosen = False
        self.__targets = None # Targets used to check which enemy/party/item is affecting who.

        # Bools to change avaliable actions.
        self.__pressed = False
        self.__can_move = True

    def move_chooser(self, direction):
        width = Initializer.SCREEN_WIDTH
        height = Initializer.SCREEN_HEIGHT
        scale = Initializer.SCALE_FACTOR

        initial_x = width / 4
        initial_y = height - scale * 14

        # Dirty way to make the positions correct based on the size of the screen.
        # Moves in fourths and then moving into the correct position.
        positions = [initial_x - scale * 9, initial_x * 2 - scale * 9, initial_x * 3 - scale * 9, initial_x * 4 - scale * 10]

        if direction == "Right":
            if self.__user_option_index != 3:
                self.__user_option_index += 1
        elif direction == "Left":
            if self.__user_option_index != 0:
                self.__user_option_index -= 1
        
        self.__user_option_chosen.set_position((positions[self.__user_option_index], initial_y))

    def check_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and self.__pressed == False:
                self.__pressed = True

                if self.__mode_chosen == False:
                    if event.key == pygame.K_LEFT:
                        self.move_chooser("Left")
                    elif event.key == pygame.K_RIGHT:
                        self.move_chooser("Right")
                    # If the user hits enter, the mode is checked in Battle
                    elif event.key == pygame.K_KP_ENTER:
                        match self.__user_option_chosen:
                            case 0:
                                self.__mode = "Attack"
                            case 1:
                                self.__mode = "Special"
                            case 2:
                                self.__mode = "Item" 
                            case 3:
                                self.__mode = "Exit"
                else:
                    pass
                    

                          
            
            if event.type == pygame.KEYUP:
                self.__pressed = False
    
    def get_mode(self):
        return self.__mode

    def get_targets(self):
        return self.__targets

    def reset(self):
        self.__mode = None
        self.__mode_chosen = False
        self.__targets = None

    def update(self):
        if self.__can_move:
            self.check_inputs()

    def draw(self, screen):
        self.__drawn_sprites.draw(screen)

    