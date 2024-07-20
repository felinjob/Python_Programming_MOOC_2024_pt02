# # WRITE YOUR SOLUTION HERE:
import pygame, math

pygame.init()
width, height = 640, 480

window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

right, down = 0, 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    window.fill((0,0,0))
    window.blit(robot, (right, down))
    pygame.display.flip()
    
    
    
    right += velocity
    if velocity > 0 and right + robot.get_width() >= width:
        for i in range(height - robot.get_height()):
            down += velocity
            window.blit(robot, (right, down))
            pygame.display.flip()   
            clock.tick(60)
        velocity = -velocity
    if velocity < 0 and right <= 0:
        for i in range(height - robot.get_height()):
            down += velocity
            window.blit(robot, (right, down))
            pygame.display.flip()   
            clock.tick(60)
        velocity = -velocity
        
    clock.tick(60)