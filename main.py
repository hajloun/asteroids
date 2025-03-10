import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
from shot import Shot


def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_running = True
BLACK = (0, 0, 0)
dt = 0
clock = pygame.time.Clock()
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Asteroid.containers = (asteroids,updatable, drawable)
Shot.containers = (shots, updatable, drawable)
AsteroidField.containers = updatable
Player.containers = (updatable, drawable)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()


while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    updatable.update(dt)
    for obj in asteroids:
        if player.collision_check(obj):
            print("Game over!")
            game_running = False
    screen.fill(BLACK)
    for obj in drawable:
            obj.draw(screen)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()