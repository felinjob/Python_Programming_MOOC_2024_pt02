# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

width, height = 640, 480

window = pygame.display.set_mode((width, height))
ball = pygame.image.load("ball.png")


ball_w = ball.get_width()
ball_h = ball.get_height()
clock = pygame.time.Clock()
x = width/2
y = height/2
x_sp = 1
y_sp = 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()


    if x + ball_w >= width or x <= 0:
        x_sp = -x_sp
    if y + ball_h >= height or y <= 0:
        y_sp = -y_sp
    
    x += x_sp
    y += y_sp

    clock.tick(120)
    
    print(x, y)
    
