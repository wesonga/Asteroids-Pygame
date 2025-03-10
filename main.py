import os
import pygame
from constants import *  # Import predefined SCREEN_WIDTH and SCREEN_HEIGHT
from player import Player  # Import Player class
from asteroidfield import AsteroidField  # Import AsteroidField class
from shot import Shot  # Import Shot class

# Function to load the high score from a file
def load_high_score():
    if os.path.exists("high_score.txt"):  # Check if the file exists
        with open("high_score.txt", "r") as file:
            return int(file.read())  # Read and return the high score
    return 0  # If the file doesn't exist, return 0 as default high score

# Function to save the current score as the new high score if it's higher
def save_high_score(score):
    with open("high_score.txt", "w") as file:
        file.write(str(score))  # Write the new high score to the file
        
# Function to create a smooth color effect for the score
def interpolate_color(value, max_value, start_color, end_color):
    ratio = value / max_value
    r = start_color[0] + (end_color[0] - start_color[0]) * ratio
    g = start_color[1] + (end_color[1] - start_color[1]) * ratio
    b = start_color[2] + (end_color[2] - start_color[2]) * ratio
    return (int(r), int(g), int(b))

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
    
    # Initialize score
    score = 0  # Score variable
    high_score = load_high_score()  # Load high score
    score_flash = False  # Flag to track score flash effect
    flash_timer = 0  # Timer for score flash duration

    # Font for score display
    font = pygame.font.Font(None, 36)  # Font for displaying the score
    
    # Color variables
    score_color = (255, 255, 255)  # Default white score color
    flash_color = (255, 223, 0)  # Gold color for flash effect
    
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
                        score += 100  # Increment the score for destroying an asteroid
                        score_flash = True  # Trigger score flash effect
                        flash_timer = 0  # Reset flash timer
                        break  # Exit the loop once the asteroid and shot collide

            # Check for collision between player and asteroid (game over)
            distance = asteroid.position.distance_to(player.position)
            if distance < asteroid.radius + player.radius:  # If collision occurs
                print("Game Over! You crashed into an asteroid!")
                pygame.quit()  # Quit the game
                return  # Exit the game loop

        # Update the flash timer if flash effect is active
        if score_flash:
            flash_timer += dt
            # print(f"Flash Timer: {flash_timer}")  # Debug print to track timer
            if flash_timer > 0.5:  # After 0.5 seconds, stop flashing
                score_flash = False
                # print("Flash effect ended!")  # Debug print when flashing ends
        
        # Smooth color interpolation for score
        score_color = interpolate_color(score, high_score + 100, (255, 255, 255), (255, 0, 0))  # From white to red
    
        # Fill screen with black
        screen.fill((0, 0, 0))
        
        # Draw all objects in the drawable group
        for drawable_obj in drawable:
            drawable_obj.draw(screen)

        # Draw all shots in the player's shots group
        for shot in player.shots:  # Iterate over the shots group
            shot.update(dt)  # Update shot position
            shot.draw(screen)  # Draw the shot
        
        # Render the score text and display it
        score_text = font.render(f"Score: {score}", True, flash_color if score_flash else score_color)  # Flash effect if triggered
        screen.blit(score_text, (10, 10))  # Display the score at the top-left corner
        
        # Render the high score text
        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(high_score_text, (SCREEN_WIDTH - 200, 10))  # Display at the top-right corner

        # Update display
        pygame.display.flip()
        
        # Update the high score if needed
        if score > high_score:
            high_score = score
            save_high_score(high_score)  # Save the new high score

        # Limit FPS to 60 and calculate delta time
        dt = clock.tick(60) / 1000  # dt will be used later for smooth movement

if __name__ == "__main__":
    main()
