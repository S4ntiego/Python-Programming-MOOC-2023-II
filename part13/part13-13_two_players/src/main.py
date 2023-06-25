# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 640 - robot.get_width() - 80
y = 480 - robot.get_height() - 80

x2 = 80
y2 = 80

to_right = False
to_left = False
to_up = False
to_down = False

to_w = False
to_s = False
to_a = False
to_d = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_a:
                to_a = True
            if event.key == pygame.K_d:
                to_d = True
            if event.key == pygame.K_w:
                to_w = True
            if event.key == pygame.K_s:
                to_s = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_a:
                to_a = False
            if event.key == pygame.K_d:
                to_d = False
            if event.key == pygame.K_w:
                to_w = False
            if event.key == pygame.K_s:
                to_s = False

        if event.type == pygame.QUIT:
            exit()

    if to_right and x <= 640 - robot.get_width():
        x += 2
    if to_left and x >= 0:
        x -= 2
    if to_up and y >= 0:
        y -= 2
    if to_down and y <= 480 - robot.get_height():
        y += 2

    if to_d and x2 <= 640 - robot.get_width():
        x2 += 2
    if to_a and x2 >= 0:
        x2 -= 2
    if to_w and y2 >= 0:
        y2 -= 2
    if to_s and y2 <= 480 - robot.get_height():
        y2 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
