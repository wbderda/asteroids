from typing import override

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float) -> None:
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.Vector2 = pygame.Vector2(x, y)
        self.velocity: pygame.Vector2 = pygame.Vector2(0, 0)
        self.radius: float = radius

    def draw(self, screen) -> None:
        # sub-classes must override
        pass

    @override
    def update(self, dt: float) -> None:
        # sub-classes must override
        pass
