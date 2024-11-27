import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    _ = pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock: pygame.time.Clock = pygame.time.Clock()
    dt = 0
    player: Player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)
        _ = screen.fill(color="black")
        player.draw(screen)
        pygame.display.flip()
        dt: float = clock.tick(framerate=60) / 1000


if __name__ == "__main__":
    main()
