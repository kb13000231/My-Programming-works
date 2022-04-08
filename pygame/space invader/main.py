import pygame
import os
# import time
# import random

pygame.init()
WIDTH = 600
HEIGHT = 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
MAIN_FONT = pygame.font.SysFont('comicsans', 40)


# load images
REDSHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_red_small.png"))
BLUESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_blue_small.png"))
GREENSHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_green_small.png"))
# player ship
YELLOWSHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RLASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
BLASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GLASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
YLASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.image.load(os.path.join("assets", "background-black.png"))
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

FPS = 60
WHITE = (255, 255, 255)


class Ship():
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cooldown = 0

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0),
                              (self.x, self.y, 50, 50))


def main():
    run = True
    level = 1
    lives = 5
    clock = pygame.time.Clock()

    ship = Ship(240, 520)

    def redraw_win():
        WIN.blit(BG, (0, 0))
        level_text = MAIN_FONT.render(
            f'Lives remaining: {lives}', 1, WHITE)
        WIN.blit(level_text, (WIDTH - level_text.get_width() - 10, 10))

        lives_text = MAIN_FONT.render(f'Level: {level}', 1, WHITE)
        WIN.blit(lives_text, (10, 10))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_win()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == '__main__':
    main()
