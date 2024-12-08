import random
from typing import override

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius=radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            new_velocity_1 = self.velocity.rotate(angle)
            new_velocity_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_velocity_1*1.2
            new_asteroid_2.velocity = new_velocity_2*1.2
            return new_asteroid_1, new_asteroid_2

