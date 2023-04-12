import pygame
from pygame.locals import *

import random

#tamanho da tela
size = width, height = (800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
speed = 1

#cores
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
gray = (128, 128, 128)
yellow = (255, 255, 30)

pygame.init()
running = True
# Define o tamanho da tela
screen = pygame.display.set_mode(size)
# Define o título da janela
pygame.display.set_caption("Cuidado com o buraco!")
# Define o background
screen.fill(green)

redCar = pygame.image.load('redCar.png')
redCar = pygame.transform.scale(redCar, (int(width/9), int(height/7)))
car_loc = redCar.get_rect()
car_loc.center = (right_lane, height*0.9)

blueCar = pygame.image.load('blueCar.png')
blueCar = pygame.transform.scale(blueCar, (int(width/9), int(height/7)))
car2_loc = blueCar.get_rect()
car2_loc.center = (left_lane, height*0.1)

cont = 0

while running:
    if cont == 2334:
        cont = 0
        speed += 1

    cont += 1
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = (left_lane, height*0.1)
        else:
            car2_loc.center = (right_lane, height*0.1)
    
    if car_loc.colliderect(car2_loc):
        print("colidiu")
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in [K_LEFT, K_a]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_RIGHT, K_d]:
                car_loc = car_loc.move([int(road_w/2), 0])
            
    #cria a pista
    pygame.draw.rect(screen, gray, (width/2 - road_w/2 , 0, road_w, height))
    #cria as faixas
    pygame.draw.rect(screen, white, (width/2 - road_w/2 + roadmark_w, 0, roadmark_w, height))
    pygame.draw.rect(screen, white, (width/2 + road_w/2 - roadmark_w*2, 0, roadmark_w, height))
    pygame.draw.rect(screen, yellow, (width/2 - roadmark_w/2, 0, roadmark_w, height))

    screen.blit(redCar, car_loc)
    screen.blit(blueCar, car2_loc)
    pygame.display.update()

pygame.quit()