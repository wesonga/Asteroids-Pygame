# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *  # Import predefined SCREEN_WIDTH and SCREEN_HEIGHT
from player import Player # Import Player class
from asteroidfield import AsteroidField # Import AsteriodField class
from shot import Shot  # Import Shot class

def main():
    pygame.init()  # Initialize pygame

    # Set up the screen with the given width and height
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock for controlling FPS
    clock = pygame.time.Clock()
    dt = 0  # Delta time placeholder
    
    # Instantiate Player in center of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

     # Create groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()  # New group for asteroids
    shots = pygame.sprite.Group()  # Group for shots

    # Add the player to both groups
    updatable.add(player)
    drawable.add(player)
    
    # Create AsteroidField object and set containers
    asteroid_field = AsteroidField(updatable, drawable, asteroids)  # Pass the groups to AsteroidField
    
    # Game loop
    while True:
        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Exit the game loop if user closes window
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Spacebar pressed
                    player.shoot()  # Call shoot method to create a bullet

        # Update player state (rotation)
        updatable.update(dt)
        asteroid_field.update(dt)  # Call update for AsteroidField
        
         # Check for collisions with asteroids and shots
        for asteroid in asteroids:
            for shot in player.shots:
                if shot is not None:
                    distance = asteroid.position.distance_to(shot.position)
                    if distance < asteroid.radius:
                        asteroid.kill()  # Destroy the asteroid
                        shot.kill()  # Destroy the shot
                        asteroid.split(updatable, drawable, asteroids)  # Split the asteroid into smaller ones
                        break  # Exit the loop once the asteroid and shot collide

            # Check for collision between player and asteroid (game over)
            distance = asteroid.position.distance_to(player.position)
            if distance < asteroid.radius + player.radius:  # If collision occurs
                print("Game Over! You crashed into an asteroid!")
                pygame.quit()  # Quit the game
                return  # Exit the game loop
            
        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Draw all objects in the drawable group
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        # Draw all shots in the player's shots group
        for shot in player.shots:  # Iterate over the shots group
            shot.update(dt)  # Update shot position
            shot.draw(screen)  # Draw the shot

        # Update display
        pygame.display.flip()

        # Limit FPS to 60 and calculate delta time
        dt = clock.tick(60) / 1000  # dt will be used later for smooth movement

if __name__ == "__main__":
    main()
