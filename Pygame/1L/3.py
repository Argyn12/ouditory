import pygame
import sys

FPS  = 80
W = 1500
H = 700
WHITE = (255, 255, 255)
YELLOU = (0, 255, 255)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys .exit()