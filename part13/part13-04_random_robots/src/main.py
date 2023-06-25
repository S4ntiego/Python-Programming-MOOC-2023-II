# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
width, height = robot.get_size()
for i in range(0, 1000):
    random_x = randint(0, 640 - width)
    random_y = randint(0, 480 - height)
    window.blit(robot, (random_x, random_y))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
