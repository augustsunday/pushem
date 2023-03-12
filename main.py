import pygame
from pushem.constants import WIDTH, HEIGHT
from pushem.board import Board
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
FPS = 60
pygame.display.set_caption("PushEm")


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_grid(WIN)
        pygame.display.update()


    pygame.quit()

main()



