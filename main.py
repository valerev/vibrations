import numpy as np
# from matplotlib import pyplot as plt
import pygame
from pygame.draw import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen_x_size = 1000
screen_y_size = 500
screen = pygame.display.set_mode((screen_x_size, screen_y_size ))
FPS = 25
screen.fill(WHITE)


class Ball:
    __radius = 1e-4
    __mass = 1e-3
    __mu = 0.5
    __dt = 1e-2
    __k = 20
    is_gravity = True

    def __init__(self, x, v, a):
        self.x = x
        self.v = v
        self.a = a
        self.neighbours = []

    def find_neighbours(self):
        self.neighbours = []
        for ball in Balls:
            if ball != self:
                if np.sqrt(np.sum((ball.x - self.x)**2)) <= 4*Ball.get_radius():
                    self.neighbours.append(ball)

    def collide_with_ball(self):
        self.a = np.array([0, -g]) * int(Ball.is_gravity)
        for ball in self.neighbours:
            self.a = self.a + Ball.__k * (self.x - ball.x)

    def collide_with_walls(self):
        if self.x[1] <= earth + 10 * Ball.get_radius():
            self.a[1] = self.a[1] + Ball.__k * 

    def move(self):
        self.x = self.x + self.v * Ball.__dt + \
                  0.5 * self.a * Ball.__dt**2
        self.v = self.v + self.a * Ball.__dt

    def draw(self):
        circle(screen, BLACK, (int(self.x[0]*500), int(self.x[1]*250)), 1)

    @staticmethod
    def get_dt():
        return Ball.__dt

    @staticmethod
    def get_radius():
        return Ball.__radius


Time = 2
earth = 0.02
g = 9.81
number_of_balls = 2


# Balls = [Ball(np.array([(2*j + 1)*Ball.get_radius() % 2500,
#                         20 + 2*Ball.get_radius()*(j//2500)]),
#               np.array([0, 0]),
#               np.array([0, -g]))
#          for j in range(number_of_balls)]

Balls = [Ball(np.array([0.25 + 200*i*Ball.get_radius(), 1]),
              np.array([0.005 * (-1)**i, 0]),
              np.array([0, 0]))
         for i in range(number_of_balls)]

Size = (0.5,)


pygame.display.update()
finished = False
clock = pygame.time.Clock()
while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.quit()
    for ball in Balls:
        ball.find_neighbours()
        ball.collide_with_ball()
        ball.collide_with_walls()
    for ball in Balls:
        ball.move()
        ball.draw()
    pygame.display.update()