from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

while True:
    back(200)
    left(170)
    if abs(pos()) < 1:
        break

left(90)
forward(100)
while True:
    forward(200)
    left(170)
    if abs(pos()) < 100:
        break

backward(200)
while True:
    back(200)
    left(170)
    if abs(pos()) < 100:
        break

end_fill()
done()
