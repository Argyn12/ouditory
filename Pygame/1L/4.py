import pygame
import time
import random
from pygame import mixer

pygame.init()
display_width = 700
display_height = 700
car_height = 200
car_width = 50
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Форсаж")
clock = pygame.time.Clock()
carImg = pygame.image.load("car1.png")
carImg = pygame.transform.scale(carImg, (70, 140))
car2Img = pygame.image.load("car2.png")
car2Img = pygame.transform.scale(car2Img, (70, 140))
coin_Img = pygame.image.load("coin.png")
coin_Img = pygame.transform.scale(coin_Img, (50, 50))
bgImg = pygame.image.load("roadbg.png")
bgImg = pygame.transform.scale(bgImg, (700, 700))
count = 0

car_x = ((display_width / 2) - (car_width / 2))
car_y = (display_height - car_height) + 50
car_x_change = 0
road_start_x = display_width - display_width
road_end_x = display_width
thing_startx = random.randrange(road_start_x, road_end_x - car_width)
thing_starty = -600
coin_x = random.randrange(road_start_x, road_end_x - car_width)
coin_y = random.randrange(0, 400)
coin_speed = 5
thing_speed = 5
thingh = 40
thingw = 40
gameExit = False
n = 10

def crash(x, y):
    time.sleep()

def draw_enemy(thingx, thingy, thing):
    gameDisplay.blit(thing, (thingx, thingy))


def draw_coin(coin_x, coin_y, coinImg):
    gameDisplay.blit(coinImg, (coin_x, coin_y))


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                car_x_change = -10
            elif event.key == pygame.K_RIGHT:
                car_x_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                car_x_change = 0


    car_x += car_x_change

    if car_x > road_end_x - 120:
        car_x = road_end_x - 120
    if car_x < road_start_x:
        car_x = road_start_x

    coin_y += coin_speed
    thing_starty += thing_speed

    if coin_y > display_height:
        coin_x = random.randrange(road_start_x + 30, road_end_x -150)
        coin_y = -500
    if thing_starty > display_height:
        thing_startx = random.randrange(road_start_x + 30,road_end_x - 150)
        thing_starty = -500

    print(car_x)
    gameDisplay.blit(bgImg, (0, 0))
    car(car_x, car_y)
    draw_enemy(thing_startx, thing_starty, car2Img)
    draw_coin(coin_x, coin_y, coin_Img)

    if car_y < thing_starty +thingh +100:
        if car_x >=thing_startx and car_x <= thing_startx + thingw +10:
            thing_startx = random.randrange(road_start_x, road_end_x-car_width)
            thing_starty = -600
            coin = 0
            coin_x = random.randrange(road_start_x + 30, road_end_x - 150)
            coin_y = -500
            thing_speed = 5
            # crash(160, 130)
        if car_x + car_width >= thing_startx and car_x +car_width <= thing_startx + thingw:
            thing_startx = random.randrange(road_start_x, road_end_x - car_width)
            thing_starty = -600
            count = 0
            coin_x = random.randrange(road_start_x + 30, road_end_x -150)
            coin_y = -500
            thing_speed = 5
            # crash(150, 130)
    coin_w = random.randrange(30, 50)
    coin_h = random.randrange(30, 50)
    if car_y < coin_y + coin_h / 2:
        if car_x + car_width / 2 >= car_x + coin_w / 2 and car_x - car_width/ 2 <= car_x +coin_w / 2:
            count += 1
            coin_Img = pygame.image.load('coin.png')
            coin_Img = pygame.transform.scale(coin_Img, (coin_w, coin_h))
            coin_x = random.randrange(road_start_x + 30, road_end_x - 150)
            coin_y = -500
        if car_x + car_width / 2 >= coin_x and car_x - car_width / 2 <= coin_x + coin_w / 2:
            count += 1
            coin_Img = pygame.image.load('coin.png')
            coin_Img = pygame.transform.scale(coin_Img, (coin_w, coin_h))
            coin_x = random.randrange(road_start_x + 30,road_end_x - 150)
            coin_y = -500
            if count == n:
                thing_speed += 3
                n += 10

    pygame.display.update()
    clock.tick(120)