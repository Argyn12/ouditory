import pygame
import sys

FPS = 60
bg_color = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((1500, 700))
pygame.display.set_caption("snake")
clock = pygame.time.Clock()
screen.fill(bg_color)

pygame.draw.rect(screen, (255, 0, 0), (0, 400, 400, 300))
pygame.draw.polygon(screen, (255, 255, 0), [[0, 400],[200, 150],[400, 400]])
pygame.draw.rect(screen, (128, 0, 0),(150, 550, 100, 150))
pygame.draw.rect(screen, (0, 255, 255),(30, 500, 80, 80))
pygame.draw.rect(screen, (0, 255, 255),(285, 500, 80, 80))
pygame.draw.circle(screen, (0, 0, 0), (230, 625),5)
pygame.draw.line(screen, (128, 128, 128), [400, 675], [1500, 675], 100)
pygame.draw.circle(screen, (0, 0, 0), (700, 600),30)
pygame.draw.circle(screen, (0, 0, 0), (900, 600),30)
pygame.draw.line(screen, (255, 255, 0), [730, 600], [870, 600], 5)
pygame.draw.line(screen, (255, 255, 0), [670, 600], [640, 600], 5)
pygame.draw.line(screen, (255, 255, 0), [930, 600], [960, 600], 5)
pygame.draw.line(screen, (255, 255, 0), [640, 600], [640, 480], 5)
pygame.draw.line(screen, (255, 255, 0), [640, 480], [850, 480], 5)
pygame.draw.line(screen, (255, 255, 0), [850, 480], [890, 530], 5)
pygame.draw.line(screen, (255, 255, 0), [890, 530], [950, 530], 5)
pygame.draw.line(screen, (255, 255, 0), [950, 530], [958, 600], 5)
pygame.draw.line(screen, (255, 255, 0), [890, 530], [640, 530], 5)
pygame.draw.polygon(screen, (0, 0, 255), [[640, 480],[850, 480],[890,530], [640, 530]])
run = True
while run:

    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()