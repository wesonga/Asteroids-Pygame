import pygame
from constants import *
from circleshape import CircleShape  # CircleShape is defined here
from shot import Shot  # Import Shot class

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # Call parent constructor with radius
        self.rotation = 0  # Initial rotation to 0
        self.shots = pygame.sprite.Group()  # Initialize the shots group
        self.shoot_timer = 0  # Timer to control shoot cooldown

    def shoot(self):
        # Only shoot if the cooldown is over (shoot_timer is 0)
        if self.shoot_timer <= 0:
            # Calculate the tip of the triangle (the front)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Front vector (tip direction)
            shoot_position = self.position + forward * self.radius  # The bullet will come from the tip of the triangle

            # Create a new shot at the tip of the player
            shot = Shot(shoot_position.x, shoot_position.y)

            # Calculate shot velocity based on player angle (rotate in the direction player is facing)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED  # Shoot in the forward direction
            self.shots.add(shot)  # Add the shot to the shots group
            self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # Reset the shoot timer after shooting


    # Move the player based on delta time (dt)
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # Calculate forward vector
        self.position += forward * PLAYER_SPEED * dt  # Update position

    # Method to define the triangle shape
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Rotate the player based on delta time (dt)
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # Update rotation based on turn speed

    # Update method to handle keypresses and update player state
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d]:
            self.rotate(dt)   # Rotate right

        if keys[pygame.K_w]:
            self.move(dt)  # Move forward
        if keys[pygame.K_s]:
            self.move(-dt)  # Move backward

        # Decrease the shoot timer by dt (time passed since the last frame)
        if self.shoot_timer > 0:
            self.shoot_timer -= dt

    # Draw method override
    def draw(self, screen):
        # Use cyan (bright blue-green) for the triangle
        pygame.draw.polygon(screen, (0, 255, 255), self.triangle(), 2)  # Change to cyan

