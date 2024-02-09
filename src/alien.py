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

# image constants
TXT_STATIC = 0
TXT_MOVE = 1

class Alien(arcade.Sprite):

    def __init__(self, scaling, sprite_size, left=1):
        super().__init__(scale=scaling)

        # set working directory to be able to reference local resources
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

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

        # oscilate between static and moving positions
        if self.txt_num == TXT_STATIC:
            self.texture = self.textures[TXT_MOVE]
            self.txt_num = TXT_MOVE
        elif self.txt_num == TXT_MOVE:
            self.texture = self.textures[TXT_STATIC]
            self.txt_num = TXT_STATIC
        
        # update position
        new_x = self.center_x

        # determine if it is moving right or left
        new_x += self.size * self.is_right
        
        # keep aliens from going out of bounds and instead move them down a row
        if new_x > arcade.get_window().width - self.size or new_x < self.size:
            # reset x-position to previous value
            new_x = self.center_x

            # move y-position down a row
            self.center_y -= self.size
            
            # reverse movement direction
            self.is_right *= -1

        # update alien x-position
        self.center_x = new_x

if __name__ == '__main__': assert False, 'This is a class file. Please import its contents into another file.'
