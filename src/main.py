import pygame
from board import Board
from getMovements import GetMovements

pygame.init()
screen = pygame.display.set_mode((1280,640))
clock = pygame.time.Clock()
running = True
newBoard = Board()
moviments = GetMovements(newBoard)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y= pygame.mouse.get_pos()
                moviments.selectPiece(x,y)
    screen.fill("black")


    newBoard.drawBoard(screen);
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
