# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")
width, height = robot.get_size()
x = 0
start_x = 0
start_y = 0
for j in range(0, 10):
    for i in range(0, 10):
        window.blit(robot, (start_x + x + width, start_y + height))
        x += width
    x = 0
    start_x += 10
    start_y += 20

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
