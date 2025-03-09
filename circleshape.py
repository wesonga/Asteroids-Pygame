import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius

    def check_collision(self, other):
        # Check if another CircleShape (like asteroid) collides with this one
        return self.position.distance_to(other.position) < (self.radius + other.radius)
