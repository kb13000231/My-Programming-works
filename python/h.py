import turtle

turtle.color('red', 'yellow')
turtle.begin_fill()

while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

while True:
    turtle.back(200)
    turtle.left(170)
    if abs(turtle.pos()) < 1:
        break

turtle.left(90)
turtle.forward(100)
while True:
    turtle.forward(200)
    turtle.left(170)
    if abs(turtle.pos()) < 100:
        break

turtle.backward(200)
while True:
    turtle.back(200)
    turtle.left(170)
    if abs(turtle.pos()) < 100:
        break

turtle.end_fill()
turtle.done()
