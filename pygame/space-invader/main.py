import pygame

# Initializing pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("rocket.png")
pygame.display.set_icon(icon)

playImg = pygame.image.load("attacker.png")
playerX = 370
playerY = 480
playerX_vel = 0


def player(x, y):
    screen.blit(playImg, (x, y))


def main():
    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    pass
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    pass

        player(playerX, playerY)
        pygame.display.update()


if __name__ == '__main__':
    main()
