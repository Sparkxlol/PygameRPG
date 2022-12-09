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
        self.__current_party = 0

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

        # Changes index of choice based on the user input.
        if direction == "Right" and self.__user_option_index != 3:
            self.__user_option_index += 1
        elif direction == "Left" and self.__user_option_index != 0:
            self.__user_option_index -= 1
        
        self.__user_option_chosen.set_position((positions[self.__user_option_index], initial_y))
    
    def target_chooser(self, direction):
        scale = Initializer.SCALE_FACTOR
        position = (0, 0)
        # Gets the correct group based on the current move.
        group = self.__groups["Enemies"] if self.__mode == "Attack" or self.__mode == "Special" else self.__groups["Party"]

        # Changes the index of the target based on user input.
        if direction == "Up" and self.__user_option_index != 0:
            self.__user_option_index -= 1
        elif direction == "Down" and self.__user_option_index != len(group) - 1:
            self.__user_option_index += 1
        
        position = group.sprites()[self.__user_option_index].get_position()        
        self.__user_option_chosen.set_position((position[0] + scale * 17, position[1] + scale * 5))

    def check_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if self.__can_move:

                if event.type == pygame.KEYDOWN and self.__pressed == False:
                    self.__pressed = True

                    if not self.__mode_chosen:
                        if event.key == pygame.K_LEFT:
                            self.move_chooser("Left")
                        elif event.key == pygame.K_RIGHT:
                            self.move_chooser("Right")
                        # If the user hits enter, the mode is checked in Battle
                        elif event.key == pygame.K_RETURN:
                            match self.__user_option_index:
                                case 0:
                                    self.__mode = "Attack"
                                case 1:
                                    self.__mode = "Special"
                                case 2:
                                    self.__mode = "Item" 
                                case 3:
                                    self.__mode = "Exit"

                            self.__mode_chosen = True
                            self.__user_option_index = 0
                            self.target_chooser("None")
                    
                    # Allows enemy/party selection.
                    else:
                        if event.key == pygame.K_UP:
                            self.target_chooser("Up")
                        elif event.key == pygame.K_DOWN:
                            self.target_chooser("Down")
                        elif event.key == pygame.K_RETURN:
                            group = self.__groups["Enemies"] if self.__mode == "Attack" or self.__mode == "Special" else self.__groups["Party"]
                            self.__targets = group.sprites()[self.__user_option_index]
                            self.set_move(False)

                if event.type == pygame.KEYUP:
                    self.__pressed = False
    
    # Sets if the user can affect the UI.
    def set_move(self, move):
        self.__can_move = move

    # Returns the mode of the battle, "Attack", "Special", "Item", "Exit"
    def get_mode(self):
        return self.__mode

    # Gets the party member that is current selected.
    def get_party(self):
        return self.__current_party

    # Gets the selected target by the user.
    def get_targets(self):
        return self.__targets

    # Resets all stats to the default values. Allows sets the chooser to default position, and allows user input.
    def reset(self):
        self.__mode = None
        self.__mode_chosen = False
        self.__targets = None
        self.__can_move = True
        self.__user_option_index = 0
        self.move_chooser("None")

    def update(self):
        self.check_inputs()

    def draw(self, screen):
        self.__drawn_sprites.draw(screen)

    