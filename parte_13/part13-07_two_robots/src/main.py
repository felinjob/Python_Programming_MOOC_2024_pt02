# WRITE YOUR SOLUTION HERE:
import pygame
import math



pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot1 = pygame.image.load("robot.png")
clock = pygame.time.Clock()
x = 0
y = 0
x1 = 0
velocity = 1
velocity1 = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((0, 0, 0))
    window.blit(robot, (x, y + robot.get_width()))
    window.blit(robot1, (x1, y + robot1.get_width() * 3))
    pygame.display.flip()
    
    x += velocity
    x1 += velocity1 *2
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity
    
    if velocity1 > 0 and x1+robot1.get_width() >= 640:
        velocity1 = -velocity1
    if velocity1 < 0 and x1 <= 0:
        velocity1 = -velocity1
    clock.tick(60)



