# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
	pygame.init() #Initialize pygame

	#Set up screen with the given width and height
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	while True:
		 # Check for quit events
        	for event in pygame.event.get():
            		if event.type == pygame.QUIT:
                		return  # Exit the game loop if user closes window

        	# Fill screen with black
        	screen.fill((0, 0, 0))

	        # Update display
        	pygame.display.flip()

if __name__ == "__main__":
	main()
