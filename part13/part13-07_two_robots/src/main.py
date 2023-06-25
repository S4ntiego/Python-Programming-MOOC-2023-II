# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x_first = 0
y_first = 0
x_second = 0
y_second = 0
velocity = 1
velocity_double = 2
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x_first, robot.get_height()))
    window.blit(robot, (x_second, robot.get_height() * 2))
    pygame.display.flip()

    x_first += velocity
    if velocity > 0 and x_first + robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x_first <= 0:
        velocity = -velocity

    x_second += velocity_double
    if velocity_double > 0 and x_second + robot.get_width() >= 640:
        velocity_double = -velocity_double
    if velocity_double < 0 and x_second <= 0:
        velocity_double = -velocity_double

    clock.tick(60)
