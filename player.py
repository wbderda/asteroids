from typing import override

import pygame
from pygame.key import ScancodeWrapper

from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED


class Player(CircleShape):
    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation: float = 0

    # in the player class
    def triangle(self) -> list[pygame.Vector2]:
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(angle=self.rotation)
        right: pygame.Vector2 = (
            pygame.Vector2(0, 1).rotate(angle=self.rotation + 90) * self.radius / 1.5
        )
        a: pygame.Vector2 = self.position + forward * self.radius
        b: pygame.Vector2 = self.position - forward * self.radius - right
        c: pygame.Vector2 = self.position - forward * self.radius + right
        return [a, b, c]

    @override
    def draw(self, screen: pygame.Surface) -> None:
        _ = pygame.draw.polygon(
            surface=screen, color="white", points=self.triangle(), width=2
        )

    def rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    @override
    def update(self, dt: float) -> None:
        keys: ScancodeWrapper = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt=-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt=-dt)

    def move(self, dt: float) -> None:
        forward: pygame.Vector2 = pygame.Vector2(0, 1).rotate(angle=self.rotation)
        self.position += forward * PLAYER_SPEED * dt
