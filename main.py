import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main() -> None:
    _ = pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    asteroid_field: AsteroidField = AsteroidField()
    dt = 0
    player: Player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        for obj in asteroids:
            if obj.check_collision(player):
                print("Game Over!")
                return
        _ = screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt: float = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
