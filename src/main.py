######################################################################################################################################################
# Name: James A. Chase
# File: main.py
# Date: 30 January 2024
# Description:
#
# Main file for Galactic Infiltrators game.
#
######################################################################################################################################################

# imports
from game import Game
from arcade import run

def main() -> None:
    '''
    Main Function

    Parameters: None

    Returns: None
    '''
    game = Game()
    game.setup()
    run()

# run main
if __name__ == '__main__': main()
