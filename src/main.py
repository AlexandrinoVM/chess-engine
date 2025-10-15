import pygame
from board import Board


pygame.init()
screen = pygame.display.set_mode((1280,640))
clock = pygame.time.Clock()
running = True
newBoard = Board()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")


    newBoard.drawBoard(screen);
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
