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
    Game(800, 600, "Galactic Infiltrators")
    run()

# run main
if __name__ == '__main__': main()
