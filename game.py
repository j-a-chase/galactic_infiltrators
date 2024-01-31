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

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def on_draw(self):
        arcade.start_render()

if __name__ == '__main__': assert False, "This is a class file. Please import its contents into another file."
