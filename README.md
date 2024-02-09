# Overview

I discovered that Python had another module for making games called Arcade! I took a brief look into it and LOVED what I saw! I've used pygame before for a few different fun game projects, but I really wanted to see where this one could go! This game in it's current state is my take on a Space Invaders game. I used to play Space Invaders with my dad when I was younger and so I really wanted to see if I could make something similar!
There's still a lot of features I would like to add, which are listed below, and things I'd love to continue exploring as I have fallen in love with this module! It's so much fun to use and is very versatile.
The game is played by moving your mouse back and forth to move your spaceship side to side. You have three lives, and taking damage from an alien removes one life, although I haven't made a display for the life system yet. If you run out of lives, that's game over! Additionally, if the aliens make it to the bottom of the screen and run into you, it's game over! You click the mouse to fire and in the current state of the game, one shot kills an alien.
I hope to be able to add more levels with various types of enemies, as well as a better scoring system and another feature or two in the future!

[Software Demo Video](https://youtu.be/7iDt1P92oUU)

# Development Environment

I used VSCode to develop this game, with Python as the language and the Arcade module being the main focus of the project. I also had to use the 'os' module to manage pathing to the correct resources, as well as the 'random' module to customize the firing rates of the aliens.

Additionally, I used Microsoft Paint to design and then scale up an alien sprite to use as a proof of concept. For those familiar with Space Invaders, you'll recognize the sprite's design. I used it as a temporary design so that I could get my game working, and I plan to remove it and design my own custom alien images as I continue to develop the game!

# Useful Websites

* [The Python Arcade Library](https://api.arcade.academy/en/latest/index.html)

# Future Work

* [] Add more levels
* [] Add start and game over screens
* [] Add more alien types
* [] Add life system to GUI
* [] Add ability to save and load game progress for different levels
* [] Add difficulty modes