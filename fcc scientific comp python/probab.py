import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for i in kwargs.keys():
            self.contents += [i]*kwargs[i]

    def draw(self, num_draws):
        balls = random.sample(self.contents, num_draws) if num_draws < len(self.contents) else self.contents
        if num_draws >= len(self.contents):
            self.contents = []
        else:
            for i in range(len(balls)):
                self.contents.remove(balls[i])
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat_balls = copy.deepcopy(hat.contents)
    correct = 0
    for i in range(num_experiments):
        hat.contents = list(hat_balls)
        draws = hat.draw(num_balls_drawn)
        draw = {}
        for i in draws:
            draw[i] = draw.get(i, 0) + 1
        coun = 0
        for i in expected_balls.keys():
            if draw.get(i, 0) >= expected_balls[i]:
                coun += 1
        if coun == len(expected_balls):
            correct += 1
    return correct/num_experiments
