import sys
import pygame
import Initializer
from Initializer import BattleInitializer
from Spritesheet import Spritesheet

class BattleUI():
    def __init__(self, groups):
        # UI Materials: Background, Buttons, etc.
        self.__itemUI = BattleItemUI(groups["Items"])
        self.__background = BattleInitializer.create_background()
        self.__user_options = Spritesheet("battleUI") # General UI
        self.__user_options.set_position((0, Initializer.SCREEN_HEIGHT - Initializer.SCALE_FACTOR * 20))
        self.__user_option_index = 0
        self.__user_option_chosen = Spritesheet("battleUIChosen") # Chosen option.
        self.__user_chosen = Spritesheet("battleUIUser") # Chosen party member.
        self.__text = []
        self.move_chooser("None")

        # Groups to draw sprites
        self.__drawn_sprites = pygame.sprite.Group()
        self.__drawn_sprites.add(self.__background)
        self.__drawn_sprites.add(self.__user_options)
        self.__drawn_sprites.add(self.__user_option_chosen)
        self.__drawn_sprites.add(self.__user_chosen)

        # Mode information: None, Attack, Special, Item, Exit
        self.__groups = groups # All enemy, party, and item sprites, needed to check positions
        self.__mode = None 
        self.__mode_chosen = False
        self.__targets = None # Targets used to check which enemy/party/item is affecting who.
        self.__current_party = 0

        # Bools to change avaliable actions.
        self.__pressed = False
        self.__can_move = True

        # Moves to current party member -> needs party position before.
        self.move_chosen()

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
        if direction == "Right" and self.__user_option_index < 3:
            self.__user_option_index += 1
        elif direction == "Left" and self.__user_option_index > 0:
            self.__user_option_index -= 1
        
        self.__user_option_chosen.set_position((positions[self.__user_option_index], initial_y))
    
    def target_chooser(self, direction):
        scale = Initializer.SCALE_FACTOR
        position = (0, 0)
        # Gets the correct group based on the current move.
        group = self.__groups["Enemies"] if self.__mode == "Attack" or self.__mode == "Special" else self.__groups["Party"]

        # Changes the index of the target based on user input.
        if direction == "Up" and self.__user_option_index > 0:
            self.__user_option_index -= 1
        elif direction == "Down" and self.__user_option_index < len(group) - 1:
            self.__user_option_index += 1
        
        position = group.sprites()[self.__user_option_index].get_position()        
        self.__user_option_chosen.set_position((position[0] + scale * 17, position[1] + scale * 5))

    def check_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Prevents movement continually.
            if event.type == pygame.KEYDOWN and self.__pressed == False:
                self.__pressed = True
            
                if self.__can_move:
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
                                    self.__can_move = False
                                    self.__itemUI.set_move(True)
                                case 3:
                                    # Escapes to the Battle object to quit the game.
                                    self.__mode = "Exit"
                                    self.__mode_chosen = True
                                    return

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

                            # Adds the used item to the end of the targets.
                            if (self.__mode == "Item"):
                                self.__targets = (self.__targets, self.__itemUI.get_item())

                            self.set_move(False)
                
                elif self.__itemUI.get_move():
                    if event.key == pygame.K_LEFT:
                        self.__itemUI.move_chooser("Left")
                    elif event.key == pygame.K_RIGHT:
                        self.__itemUI.move_chooser("Right")
                    # If the user hits enter, the mode is checked in Battle
                    elif event.key == pygame.K_RETURN:
                        self.__itemUI.hold_item()
                        self.__itemUI.set_move(False)
                        self.__can_move = True
                    elif event.key == pygame.K_ESCAPE:
                        self.reset()

            if event.type == pygame.KEYUP:
                self.__pressed = False
                    
    # Moves the chosen box around whoever the current party is.
    def move_chosen(self):
        chosen_pos = self.__groups["Party"].sprites()[self.__current_party].get_position()
        self.__user_chosen.set_position((chosen_pos[0] - 1 * Initializer.SCALE_FACTOR, chosen_pos[1] - 1 * Initializer.SCALE_FACTOR))
    
    # Creates text above an enemy indicating its change in health.
    def create_damage_text(self, value, target_position):
        if value == None:
            return

        # Red or Green based on change.
        color = (255, 0, 0) if value < 0 else (0, 255, 34)
        position = (target_position[0] + 20 * Initializer.SCALE_FACTOR, target_position[1] + 5 * Initializer.SCALE_FACTOR)

        self.__text.append(TextUI(str(value), color, position))
    
    # Sets if the user can affect the UI.
    def set_move(self, move):
        self.__can_move = move

    # Returns the mode of the battle, "Attack", "Special", "Item", "Exit"
    def get_mode(self):
        return self.__mode

    # Gets the party member that is current selected.
    def get_party(self):
        return self.__current_party

    # Sets the current party members
    def set_party(self, party):
        self.__current_party = party

    # Gets the selected target by the user.
    def get_targets(self):
        return self.__targets

    # Resets all stats to the default values. Allows sets the chooser to default position, and allows user input.
    def reset(self):
        self.__mode = None
        self.__mode_chosen = False
        self.__targets = None
        self.__can_move = True
        self.__itemUI.set_move(False)
        self.__user_option_index = 0
        self.move_chooser("None")    
        self.move_chosen()

    def update(self):
        self.check_inputs()

        for text in self.__text:
            text.update()
            if text.get_time() > Initializer.FPS:
                self.__text.remove(text)

    def draw(self, screen):
        # Removes the chooser icon if the user cannot selected and vice versa.
        if (not self.__can_move and self.__drawn_sprites.has(self.__user_option_chosen)):
            self.__drawn_sprites.remove(self.__user_option_chosen)
        elif (self.__can_move and not self.__drawn_sprites.has(self.__user_option_chosen)):
            self.__drawn_sprites.add(self.__user_option_chosen)

        self.__drawn_sprites.draw(screen)

        if self.__itemUI.get_move():
            self.__itemUI.draw(screen)

        # Draws text on the screen indicating changes in the game.
        for text in self.__text:
            screen.blit(text.get_img(), text.get_rect())

class BattleItemUI:
    def __init__(self, items):
        self.__item_group = items
        self.__current_item = None
        self.__user_options = []
        self.__user_option_chosen = Spritesheet("battleUIChosen")
        self.__user_option_index = 0
        self.move_initial()

        self.__can_move = False
    
    def move_initial(self):
        # Creates a box for each of the items.
        self.__user_options = [Spritesheet("itemUI") for item in self.__item_group]
        pos = [0, 68 * Initializer.SCALE_FACTOR]
        jump = 20 * Initializer.SCALE_FACTOR
        self.__user_option_index = 0
        self.__user_option_chosen.set_position((11 * Initializer.SCALE_FACTOR, pos[1] + 2 * Initializer.SCALE_FACTOR))

        # Moves each box and item into the correct position.
        for item, box in zip(self.__item_group, self.__user_options):
            box.set_position(pos)
            item.set_position((pos[0] + 2 * Initializer.SCALE_FACTOR, pos[1] + 2 * Initializer.SCALE_FACTOR))
            pos[0] += jump

        # Adds each element to a group to draw. This is needed to prevent extra boxes from spawning around former items.
        self.__drawn_sprites = pygame.sprite.Group()
        self.__drawn_sprites.add(self.__user_options)
        self.__drawn_sprites.add(self.__user_option_chosen)
        self.__drawn_sprites.add(self.__item_group)
    
    def move_chooser(self, direction):
        # Returns if there are no items.
        if (len(self.__item_group) == 0):
            return

        max_length = len(self.__item_group)
        jump = 20 * Initializer.SCALE_FACTOR
        position = self.__user_option_chosen.get_position()

        # Moves the boxes, items and chooser to the right if need be. 
        '''
        if (position[0] >= 80 and direction == "Right") or (position[0] <= 0 and direction == "Left"):
            move_pos = [0, 0]
            if direction == "Right":
                move_pos = [self.__item_group, 68 * Initializer.SCALE_FACTOR]
            else:
                move_pos = [self.__item_group, 68 * Initializer.SCALE_FACTOR]

            for item, box in zip(self.__item_group, self.__user_options):
                box.set_position(pos)
                item.set_position((pos[0] + 2 * Initializer.SCALE_FACTOR, pos[1] + 2 * Initializer.SCALE_FACTOR))
                pos[0] += jump
        '''
        
        cur_pos = self.__user_option_chosen.get_position()
        # Moves the chooser to the right and left.
        if direction == "Right" and self.__user_option_index < max_length - 1:
            self.__user_option_index += 1
            self.__user_option_chosen.set_position((cur_pos[0] + jump, cur_pos[1]))
        elif direction == "Left" and self.__user_option_index > 0:
            self.__user_option_index -= 1
            self.__user_option_chosen.set_position((cur_pos[0] - jump, cur_pos[1]))

    # Sets currently selected item.
    def hold_item(self):
        self.__current_item = self.__item_group.sprites()[self.__user_option_index]
    
    # Returns the item being held and removes from current_item.
    def get_item(self):
        item = self.__current_item
        self.__current_item = None

        return item

    # Returns if the user can affect the items.
    def get_move(self):
        return self.__can_move

    # Sets if the user can affect the UI.
    def set_move(self, move):
        self.move_initial()
        self.__can_move = move

    def draw(self, screen):
        self.__drawn_sprites.draw(screen)

class TextUI:
    FONT = pygame.font.SysFont("Font/PixelOperator.ttf", 20)

    def __init__(self, text, color, position):
        self.__time = 0
        self.__img = pygame.transform.scale(TextUI.FONT.render(text, True, color), (Initializer.SCALE_FACTOR * 5, Initializer.SCALE_FACTOR * 5))
        self.__rect = self.__img.get_rect()
        self.__rect.x = position[0]
        self.__rect.y = position[1]
    
    def get_time(self):
        return self.__time

    def get_img(self):
        return self.__img

    def get_rect(self):
        return self.__rect

    def update(self):
        self.__time += 1