# make a fully functioning 3d dice

import random
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DICE")
FONT = pygame.font.SysFont("comicsans", 100)
roll_FONT = pygame.font.SysFont("comicsans", 50)


def draw(win):
    win.fill((0, 0, 0))


def dice(num, win, rolls, counter):
    diceroll = FONT.render(f'Current Roll: {num}', 1, (255, 0, 0))
    win.blit(diceroll, (WIDTH//2 - diceroll.get_width()//2, HEIGHT//2))
    count = FONT.render(f'Current Count: {counter}', 1, (255, 0, 0))
    win.blit(count, (WIDTH//2 - count.get_width()//2, HEIGHT//4))
    prev_rolls = roll_FONT.render('Prev_rolls: ', 1, (255, 0, 0))
    win.blit(prev_rolls, (WIDTH//2 - count.get_width()//2, 3*HEIGHT//4))
    k = len(rolls)
    if len(rolls) < 10:
        rolls = rolls[::-1]
    else:
        rolls = rolls[-10:][::-1]
    i = 0
    for rollout in rolls:
        curr_roll = roll_FONT.render(f'{rollout}', 1, (255, 0, 0))
        win.blit(curr_roll, (WIDTH//2 - count.get_width()//2 + 30*i + prev_rolls.get_width(), 3*HEIGHT//4))
        i += 1
    pygame.display.update()


def main():
    run = True
    clock = pygame.time.Clock()
    num = 0
    counter = 0
    rolls = []

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
            rolls.append(num)
            counter += 1
            dice(num, WIN, rolls, counter)
            pygame.time.delay(300)

    pygame.quit()


if __name__ == '__main__':
    main()
