import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
RADIUS = 7

SCORE_FONT = pygame.font.SysFont("comicsans", 60)
WIN_SCORE = 10


class Paddle:
    COLOR = WHITE
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self):
        self.x = self.origin_x
        self.y = self.origin_y


class Ball:
    MAX_VEL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.origin_x = x
        self.y = self.origin_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.x_vel
        self.y += int(self.y_vel)

    def reset(self):
        self.x = self.origin_x
        self.y = self.origin_y
        self.y_vel = 0
        self.x_vel *= -1

    # def freset(self):
    #     self.x = self.origin_x
    #     self.y = self.origin_y
    #     self.y_vel = 0
    #     self.x_vel = 0


def draw(win, paddles, ball, lscore, rscore):
    win.fill(BLACK)

    lscore_text = SCORE_FONT.render(f'{lscore}', 1, WHITE)
    rscore_text = SCORE_FONT.render(f'{rscore}', 1, WHITE)
    win.blit(lscore_text, (WIDTH//4 - lscore_text.get_width()//2, 20))
    win.blit(rscore_text, (WIDTH*3//4 - rscore_text.get_width()//2, 20))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, 25):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2-5, i, 10, HEIGHT//20))

    ball.draw(win)
    pygame.display.update()


def handle_paddle_movement(keys, lpad, rpad):
    if keys[pygame.K_w] and lpad.y - lpad.VEL >= 0:
        lpad.move(up=True)
    if keys[pygame.K_s] and lpad.y + lpad.VEL + lpad.height <= HEIGHT:
        lpad.move(up=False)

    if keys[pygame.K_UP] and rpad.y - rpad.VEL >= 0:
        rpad.move(up=True)
    if keys[pygame.K_DOWN] and rpad.y + rpad.VEL + rpad.height <= HEIGHT:
        rpad.move(up=False)


def handle_collisions(ball, lpaddle, rpaddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    if ball.x_vel < 0:
        if ball.y >= lpaddle.y and ball.y <= lpaddle.y + lpaddle.height:
            if ball.x - ball.radius <= lpaddle.x + lpaddle.width:
                ball.x_vel *= -1

                mid = lpaddle.y + lpaddle.height/2
                diff = ball.y - mid
                red_factor = (lpaddle.height/2)/ball.MAX_VEL
                ball.y_vel = diff/red_factor

    else:
        if ball.y >= rpaddle.y and ball.y <= rpaddle.y + rpaddle.height:
            if ball.x + ball.radius >= rpaddle.x:
                ball.x_vel *= -1

                mid2 = rpaddle.y + rpaddle.height/2
                diff = ball.y - mid2
                red_factor = (rpaddle.height/2)/ball.MAX_VEL
                ball.y_vel = diff/red_factor


def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH//2, HEIGHT//2, RADIUS)

    lscore = 0
    rscore = 0

    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle, right_paddle], ball, lscore, rscore)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        handle_collisions(ball, left_paddle, right_paddle)
        ball.move()

        if ball.x < 0:
            rscore += 1
            ball.reset()
        elif ball.x > WIDTH:
            lscore += 1
            ball.reset()

        won = False
        if lscore == WIN_SCORE:
            won = True
            win_text = "Left Player WINS!!"
        if rscore == WIN_SCORE:
            won = True
            win_text = "Right Player WINS!!"

        if won:
            text = SCORE_FONT.render(win_text, 1, WHITE)
            WIN.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            lscore = 0
            rscore = 0

    pygame.quit()


if __name__ == '__main__':
    main()
