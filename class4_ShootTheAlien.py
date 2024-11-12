#Shoot the alien
# Import the Pygame Zero Library
import pgzrun
from random import randint
# Pygame Standard for deciding the title of your game window 
TITLE = "Alien shooter"
# Pygame Standard for deciding the width and height for your game window in pixels
HEIGHT = 500
WIDTH = 500
# variable to store the message displayed on your screen
message="Max"

# Actor is built-in object in pgzero
Alien = Actor("alien1")
# interacts with other actors, move around on screen
# Similar to Sprite in Scratch
#alien.pos = 50,50



# Default function which will be called to update the screen
def draw():
  #screen is another built-in object
  screen.fill(color=(0,149,137))
  Alien.draw()
  screen.draw.text(message,(400,50))
#  place_alien()

  
def place_alien():
  Alien.pos=(randint(0,WIDTH),randint(0,HEIGHT))

place_alien()

def on_mouse_down(pos):
  #print("Hello World")
  global message
  if Alien.collidepoint(pos):
    place_alien()
    message="Amazinggg"

  else:
    message="try again"


  
# This method needs to be called to start processing
pgzrun.go()