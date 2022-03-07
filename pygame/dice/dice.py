# make a fully functioning 3d dice

import random
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DICE")
FONT = pygame.font.SysFont("comicsans", 100)


def draw(win):
    win.fill((0, 0, 0))


def dice(num, win, counter):
    diceroll = FONT.render(f'Current Roll: {num}', 1, (255, 0, 0))
    win.blit(diceroll, (WIDTH//2 - diceroll.get_width()//2, HEIGHT//2))
    count = FONT.render(f'Current Count: {counter}', 1, (255, 0, 0))
    win.blit(count, (WIDTH//2 - count.get_width()//2, HEIGHT//4))
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    num = 0
    counter = 0

    while run:
        clock.tick(60)
        draw(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            num = random.randint(1, 6)
            counter += 1
            dice(num, WIN, counter)
            pygame.time.delay(300)

    pygame.quit()


if __name__ == '__main__':
    main()
