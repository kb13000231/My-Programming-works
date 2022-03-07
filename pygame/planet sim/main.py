import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulator")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SUN = (255, 255, 0)
MERCURY = (142, 142, 142)
EARTH = (100, 150, 240)
MARS = (190, 40, 50)


class Planet:
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 225/AU  # 1AU = 100 pixels
    TIMESTEP = 86400

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.sun = False
        self.dis_to_sun = 0
        self.orbit = []

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH/2
        y = self.y * self.SCALE + HEIGHT/2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points)
        pygame.draw.circle(win, self.color, (int(x), int(y)), self.radius)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        dis_x = other_x - self.x
        dis_y = other_y - self.y
        dis = math.sqrt(dis_x ** 2 + dis_y ** 2)

        if other.sun:
            self.dis_to_sun = dis

        force = self.G * self.mass * other.mass / dis ** 2
        theta = math.atan2(dis_y, dis_x)
        x_force = math.cos(theta) * force
        y_force = math.sin(theta) * force

        return x_force, y_force

    def update_pos(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, SUN, 1.98892*10**30)
    sun.sun = True

    mercury = Planet(0.387*Planet.AU, 0, 8, MERCURY, 3.3*10**24)
    mercury.y_vel = -47.4 * 1000
    venus = Planet(0.723*Planet.AU, 0, 14, WHITE, 3.3*10**24)
    venus.y_vel = -35.02 * 1000
    earth = Planet(-1*Planet.AU, 0, 16, EARTH, 5.9742*10**24)
    earth.y_vel = 29.783 * 1000
    mars = Planet(-1.524*Planet.AU, 0, 12, MARS, 6.39*10**23)
    mars.y_vel = 24.077 * 1000

    planets = [sun, mercury, venus, earth, mars]

    while run:
        clock.tick(FPS)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_pos(planets)
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
