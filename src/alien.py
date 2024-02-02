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
TXT_FIRE = 1

class Alien(arcade.Sprite):

    def __init__(self, scaling):
        super().__init__(scale=scaling)

        # set working directory to be able to reference local resources
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

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

if __name__ == '__main__': assert False, 'This is a class file. Please import its contents into another file.'
