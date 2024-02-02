######################################################################################################################################################
# Name: James A. Chase
# File: game.py
# Date: 30 January 2024
# Description:
#
# Class file for Game class
#
######################################################################################################################################################

# imports
import arcade

# screen constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 864
SCREEN_TITLE = "Galactic Infiltrators"

# sprite constants
CHARACTER_SCALING = 1
CHARACTER_LASER_SCALING = 0.8
TILE_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# game constants
BULLET_SPEED = 5

# player starting position
PLAYER_START_X = 256
PLAYER_START_Y = 128

# layer names
LN_BACKGROUND = "Background"
LN_PLAYER = "Player"
LN_ENEMIES = "Enemies"

class Game(arcade.Window):
    def __init__(self):
        # window setup with parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)

        # tilemap object for maps
        self.tile_map = None

        # scene object for sprites
        self.scene = None

        # keeps track of the player sprite
        self.player_sprite = None

        # physics engine
        self.physics_engine = None

        # camera for gui elements
        self.gui_camera = None

        # keep track of score
        self.score = 0

        # keep track of level
        self.level = 1

        # load sounds
        self.player_laser_sound = arcade.load_sound(":resources:sounds/laser2.wav")

        # set window background color
        arcade.set_background_color(arcade.csscolor.DARK_BLUE)

    def setup(self) -> None:
        '''
        Set up game variables. Call to restart game.

        Parameters: None

        Returns: None
        '''

    def on_draw(self) -> None:
        '''
        Renders the screen.

        Parameters: None

        Returns: None
        '''
        self.clear()

    def on_update(self, delta_time) -> None:
        '''
        Contains all logic to move, and game logic.

        Parameters:
            - delta_time

        Returns: None
        '''

    def on_keypress(self, key, key_modifiers) -> None:
        '''
        Called whenever a key on the keyboard is pressed

        Parameters:
            - key
            - key_modifiers

        Returns: None
        '''

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
