import turtle
import time
import random

try:
    with open('highscore.txt', 'r') as file:
        high_score = int(file.read().split()[2])
except FileNotFoundError:
    high_score = 0

delay = 0.1
score = 0
meal_eaten = 0
special = False
curr_color = None
prev_color = None


win = turtle.Screen()
win.title('Classic Snake')
win.bgcolor('white')

win.setup(width=600, height=600)
win.tracer(0)

head = turtle.Turtle()
head.shape('square')
head.color('black')
head.penup()
head.goto(0, 0)
head.direction = 'Stop'

meal = turtle.Turtle()
shapes = ['circle', 'square', 'triangle']
colors = ['blue', 'red', "black"]
k = random.choice(shapes)
meal.speed(0)
meal.shape(k)
meal.color(random.choice(colors))
meal.penup()
meal.goto(0, 100)

score_board = turtle.Turtle()
score_board.speed(0)
score_board.shape('square')
score_board.color('black')
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 250)
score_board.write(f'Score: 0  High Score: {high_score}', align="center",
                  font=('candara', 24, 'bold'))


def goup():
    if head.direction != 'down':
        head.direction = 'up'


def godown():
    if head.direction != 'up':
        head.direction = 'down'


def goleft():
    if head.direction != "right":
        head.direction = "left"


def goright():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


win.listen()
win.onkeypress(goup, 'w')
win.onkeypress(godown, 's')
win.onkeypress(goright, 'd')
win.onkeypress(goleft, 'a')

segments = []

while True:
    try:
        win.update()
    except turtle.Terminator:
        with open('highscore.txt', 'w') as file:
            file.write(f'high_score = {high_score}')

    if not -290 <= head.xcor() <= 290 or not -290 <= head.ycor() <= 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        meal_eaten = 0
        score = 0
        delay = 0.1
        score_board.clear()
        score_board.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(meal) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        if meal_eaten == 9:
            meal.shape('turtle')
            special = True
        else:
            meal.shape(k)
            special = False
        meal.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        colors2 = ['orange', 'red', 'green', 'blue', 'yellow']
        while curr_color == prev_color:
            curr_color = random.choice(colors2)
        new_segment.color(curr_color)
        prev_color = curr_color
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        if meal_eaten == 10:
            score += 25
            meal_eaten = 0
        else:
            score += 10
            meal_eaten += 1
        if score > high_score:
            high_score = score
        score_board.clear()
        score_board.write(f"Score : {score} High Score : {high_score}",
                          align="center", font=("candara", 24, "bold"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            meal_eaten = 0
            score = 0
            delay = 0.1
            score_board.clear()
            score_board.write(f"Score : {score} High Score : {high_score} ",
                              align="center", font=("candara", 24, "bold"))
    time.sleep(delay)

win.mainloop()
