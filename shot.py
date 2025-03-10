import pygame
from constants import SHOT_RADIUS

class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((SHOT_RADIUS * 2, SHOT_RADIUS * 2))
        self.image.fill((255, 255, 0))  # Bright yellow color
        self.rect = self.image.get_rect(center=(x, y))
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  # Default velocity (will be set in Player)

    def update(self, dt):
        self.position += self.velocity * dt  # Update shot position based on velocity
        self.rect.center = self.position  # Update rect to new position

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the shot on the screen
