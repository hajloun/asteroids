import pygame
from constants import *

def main():
    numpass, numfail = init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_running = True
BLACK = (0, 0, 0)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.fill(BLACK)
    pygame.display.flip()

if __name__ == "__main__":
    main()