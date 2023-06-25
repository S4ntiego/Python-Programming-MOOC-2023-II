import pygame
import random

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

robots = []
for i in range(20):
    x = random.randint(0 + robot.get_width(), (width - robot.get_width()))
    y = random.randint(-1000, -robot.get_height())
    direction = random.choice(["left", "right"])
    robots.append((x, y, direction))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0, 0, 0))

    for i, (x, y, direction) in enumerate(robots):
        if y + robot.get_height() < height:
            y += 1
        else:
            if direction == "left":
                x -= 1
            else:
                x += 1
            if x < -robot.get_width() or x > width:
                x = random.randint(0 + robot.get_width(), (width - robot.get_width()))
                y = random.randint(-1000, -robot.get_height())
                direction = random.choice(["left", "right"])
        robots[i] = (x, y, direction)

    for x, y, _ in robots:
        screen.blit(robot, (x, y))

    pygame.display.flip()

    clock.tick(60)
