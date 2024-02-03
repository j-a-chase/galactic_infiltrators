######################################################################################################################################################
# Name: James A. Chase
# File: alien.py
# Date: 2 February 2024
# Description:
#
# Class file for Alien class
#
######################################################################################################################################################

# imports
import arcade
import os
import math

# image constants
TXT_STATIC = 0
TXT_FIRE = 1

# enemy constants
ENEMY_SPEED = 3.0

class Alien(arcade.Sprite):

    def __init__(self, scaling, sprite_size, left=1):
        super().__init__(scale=scaling)

        # set working directory to be able to reference local resources
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # keep track of unit speed
        self.speed = ENEMY_SPEED

        # keep track of unit direction
        self.is_right = 1 * left

        # keep track of unit size
        self.size = sprite_size

        # list to hold textures to oscilate between
        self.textures = []

        # which texture?
        self.txt_num = TXT_STATIC

        # add first texture
        texture = arcade.load_texture('./resources/custom_sprites/alien_basic.png')
        self.textures.append(texture)
        
        # default to first texture
        self.texture = texture

        # add second texture
        texture = arcade.load_texture('./resources/custom_sprites/alien_basic_move.png')
        self.textures.append(texture)

    def update(self):
        if self.txt_num == TXT_STATIC:
            self.texture = self.textures[TXT_FIRE]
            self.txt_num = TXT_FIRE
        elif self.txt_num == TXT_FIRE:
            self.texture = self.textures[TXT_STATIC]
            self.txt_num = TXT_STATIC
        
        # update position
        new_x = self.center_x

        new_x += self.size * self.is_right
        if new_x > arcade.get_window().width - self.size or new_x < self.size:
            new_x = self.center_x
            self.center_y -= self.size
            self.is_right *= -1
        self.center_x = new_x

        print(self.center_x, self.center_y)

if __name__ == '__main__': assert False, 'This is a class file. Please import its contents into another file.'
