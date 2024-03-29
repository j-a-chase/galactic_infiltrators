######################################################################################################################################################
# Name: James A. Chase
# File: game.py
# Date: 30 January 2024
# Description:
#
# Class file for Game class
#
######################################################################################################################################################

# module imports
import arcade
import os
import random

# class imports
from alien import Alien

# screen constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 864
SCREEN_TITLE = "Galactic Infiltrators"

# sprite constants
CHARACTER_SCALING = .75
CHARACTER_LASER_SCALING = 0.55
TILE_SCALING = 0.25
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING
ENEMY_LASER_SCALING = 0.5

# game constants
PLAYER_BULLET_SPEED = 10
BG_COLOR = (0,0,64)
ANIMATION_TIMER_CAP = 30
LVL_ONE_ENEMY_COUNT = 45
LVL_ONE_ENEMY_ROW_CAP = 5
ENEMY_BULLET_SPEED = -6
ENEMY_FIRING_ODDS = 1000

# player starting position
PLAYER_START_X = 320
PLAYER_START_Y = 96

# layer names
LN_PLAYER = "Player"
LN_ENEMIES = "Enemies"
LN_BULLETS = "Bullets"
LN_ENEMY_BULLETS = "Enemy Bullets"

class Game(arcade.Window):
    def __init__(self):
        # window setup with parent class
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window=True)

        # set working directory to be able to reference local resources
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # scene object for sprites
        self.scene = None

        # keeps track of the player sprite
        self.player_sprite = None
        self.player_lives = 0

        # camera for gui elements
        self.gui_camera = None

        # don't show mouse cursor
        self.set_mouse_visible(False)

        # keep track of score
        self.score = 0

        # keep track of level
        self.level = 1

        # load sounds
        self.player_laser_sound = arcade.load_sound(":resources:sounds/laser2.wav")
        self.enemy_hit_sound = arcade.load_sound(":resources:sounds/hit4.wav")
        self.player_hit_sound = arcade.load_sound(":resources:sounds/hurt3.wav")

        # timer for animations
        self.animation_timer = 0

        # set window background color
        arcade.set_background_color(BG_COLOR)

    def setup(self) -> None:
        '''
        Set up game variables. Call to restart game.

        Parameters: None

        Returns: None
        '''
        # setup gui camera
        self.gui_camera = arcade.Camera(self.width, self.height)

        # setup scene
        self.scene = arcade.Scene()
        self.scene.add_sprite_list(LN_PLAYER)
        self.scene.add_sprite_list(LN_ENEMIES)
        self.scene.add_sprite_list(LN_BULLETS)
        self.scene.add_sprite_list(LN_ENEMY_BULLETS)

        # animation timer for alien animations
        self.animation_timer = 0

        # setup player
        self.score = 0
        self.player_lives = 3
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.scene.add_sprite(LN_PLAYER, self.player_sprite)

        # setup enemies for level one
        if self.level == 1:
            # keeps track of total enemies generated between rows
            total_enemies = 0

            # generates enemies row by row
            for row in range(LVL_ONE_ENEMY_ROW_CAP):
                i = 0
                
                # even rows can have 10 aliens
                if row % 2 == 0:
                    while i < 10 and total_enemies < LVL_ONE_ENEMY_COUNT:
                        # generate alien instance
                        alien = Alien(TILE_SCALING, GRID_PIXEL_SIZE)

                        # position alien
                        alien.center_x = 2 * GRID_PIXEL_SIZE * i + GRID_PIXEL_SIZE
                        alien.center_y = SCREEN_HEIGHT - GRID_PIXEL_SIZE - (GRID_PIXEL_SIZE * row)

                        # add alien to sprite list and increment counters
                        self.scene.add_sprite(LN_ENEMIES, alien)
                        i += 1
                        total_enemies += 1
                # odd rows can have 9 aliens
                else:
                    while i < 9 and total_enemies < LVL_ONE_ENEMY_COUNT:
                        # generate alien instance
                        alien = Alien(TILE_SCALING, GRID_PIXEL_SIZE, left=-1)

                        # position alien
                        alien.center_x = 2 * GRID_PIXEL_SIZE * (9 - i)
                        alien.center_y = SCREEN_HEIGHT - GRID_PIXEL_SIZE - (GRID_PIXEL_SIZE * row)

                        # add alien to sprite list and increment counters
                        self.scene.add_sprite(LN_ENEMIES, alien)
                        i += 1
                        total_enemies += 1

        # set background color
        arcade.set_background_color(BG_COLOR)

    def on_draw(self) -> None:
        '''
        Renders the screen.

        Parameters: None

        Returns: None
        '''
        # clear screen before drawing
        self.clear()

        # draw scene
        self.scene.draw()

        # draw gui
        self.gui_camera.use()
        arcade.draw_text(f'Score: {self.score}', 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time) -> None:
        '''
        Contains all logic to move, and game logic.

        Parameters:
            - delta_time

        Returns: None
        '''
        # get bullet and enemy lists
        bullet_list = self.scene.get_sprite_list(LN_BULLETS)
        enemy_list = self.scene.get_sprite_list(LN_ENEMIES)
        enemy_bullet_list = self.scene.get_sprite_list(LN_ENEMY_BULLETS)

        # call update on each bullet
        bullet_list.update()
        enemy_bullet_list.update()

        # call update on each enemy
        self.animation_timer += 1
        if self.animation_timer == ANIMATION_TIMER_CAP:
            enemy_list.update()
            self.animation_timer = 0

        # check for bullet collisions
        for bullet in bullet_list:
            # collision checks for bullets to enemies
            hit_list = arcade.check_for_collision_with_list(bullet, enemy_list)
            
            # if bullet hit enemy, remove it
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # if enemy was hit, "kill" and increase score
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                self.score += 100

                # play hit sound
                arcade.play_sound(self.enemy_hit_sound)

            # if bullet goes off screen, remove it
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        # check each enemy
        for enemy in enemy_list:
            # if they've hit the player with their body
            player_is_hit = arcade.check_for_collision(enemy, self.player_sprite)

            # instant game over
            if player_is_hit:
                print('Game Over!')
                arcade.exit()

            # calculate firing odds
            odds = int(ENEMY_FIRING_ODDS * (1/60) / delta_time)

            # fire bullet if odds are there
            if random.randrange(odds) == 0:
                bullet = arcade.Sprite(':resources:images/space_shooter/laserRed01.png', ENEMY_LASER_SCALING)
                bullet.center_x = enemy.center_x
                bullet.angle = 180
                bullet.top = enemy.bottom
                bullet.change_y = ENEMY_BULLET_SPEED
                self.scene.add_sprite(LN_ENEMY_BULLETS, bullet)

        # check each enemy bullet
        for bullet in enemy_bullet_list:
            # if it hits the player
            player_is_hit = arcade.check_for_collision(bullet, self.player_sprite)

            # deal damage and remove a life
            if player_is_hit:
                arcade.play_sound(self.player_hit_sound)
                self.player_lives -= 1
                print(f'{self.player_lives} lives left!')
                bullet.remove_from_sprite_lists()

            # if enemy bullet goes off bottom of screen, remove bullet
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()
            
            # if player lives are zero, end game.
            if self.player_lives == 0:
                print('Game Over!')
                arcade.exit()

    def on_mouse_motion(self, x, y, dx, dy) -> None:
        '''
        Called whenever the mouse moves.

        Parameters:
            - x
            - y
            - dx
            - dy

        Returns: None
        '''
        # move player ship to where mouse is positioned x-wise
        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers) -> None:
        '''
        Called whenever the mouse button is clicked

        Parameters:
            - x
            - y
            - button
            - modifiers

        Returns: None
        '''
        # fire laser
        arcade.play_sound(self.player_laser_sound)
        bullet = arcade.Sprite(":resources:/images/space_shooter/laserBlue01.png", CHARACTER_LASER_SCALING)
        
        # rotate laser image
        bullet.angle = 90

        # set bullet speed
        bullet.change_y = PLAYER_BULLET_SPEED

        # position laser
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        # add to sprite list
        self.scene.add_sprite(LN_BULLETS, bullet)

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
