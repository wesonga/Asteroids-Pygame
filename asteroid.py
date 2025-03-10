import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Set the color for the asteroid
        self.color = random.choice([(255, 165, 0), (128, 0, 128), (255, 0, 0), (255, 255, 0)])  # Random color


        self.velocity = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) * ASTEROID_SPEED
    
    def draw(self, screen):
         # Draw the asteroid with the assigned color
        pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, updatable, drawable, asteroids):
        self.kill()  # Kill the current asteroid

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1

        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2

        # Add the new asteroids to the relevant groups
        updatable.add(asteroid1)
        drawable.add(asteroid1)
        asteroids.add(asteroid1)

        updatable.add(asteroid2)
        drawable.add(asteroid2)
        asteroids.add(asteroid2)
