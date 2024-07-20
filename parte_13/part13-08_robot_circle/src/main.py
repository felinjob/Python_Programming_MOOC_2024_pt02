# WRITE YOUR SOLUTION HERE:
import pygame, math
from random import randint
pygame.init()

width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
angle = 0
rad = 150
rob_w = robot.get_width()
rob_h = robot.get_height()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    window.fill((0,0,0))
    for i in range(10):  
        x = width/2+math.cos(angle+2*math.pi*i/10)*rad-rob_w/2
        y = height/2+math.sin(angle+2*math.pi*i/10)*rad-rob_h/2
        window.blit(robot, (x, y))
    pygame.display.flip()

    
    angle += 0.01
    clock.tick(60)