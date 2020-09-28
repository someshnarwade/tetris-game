import sys

import pygame

# TODO Add Shapes {S: 2, Z: 2, L: 4, Flipped_L: 4, I: 2, B: 1}


pygame.init()

SIZE = WIDTH, HEIGHT = (800, 600)
speed = [1, 1]
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (50, 50, 50)
TEAL = (0, 247, 222)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("TETRIS")


def grid_init():
    for c in range(275, 525, 25):
        for r in range(100, 600, 25):
            pygame.draw.rect(screen, GREY, ((c, r), (25, 25)), 1)
    pygame.draw.rect(screen, RED, ((275, 100), (250, 500)), 2)
    pass


game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # screen.fill(BLACK)
    grid_init()

    pygame.display.flip()
