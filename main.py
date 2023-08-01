import sys
from grid import Grid
from game import Game
from color import Color
import pygame
pygame.init()


game = Game()

TOP_BAR_HEIGHT = 200
screen = pygame.display.set_mode(
    (game.WIDTH, game.HEIGHT + TOP_BAR_HEIGHT)
)

pygame.display.set_caption("Sudoku solver")
FPS = 60

clock = pygame.time.Clock()


def draw():
    # screen.fill(Color.RED)
    game.draw(screen, (0, TOP_BAR_HEIGHT))
    pygame.display.update()


def main() -> None:
    running = True
    
    while running:
        clock.tick(FPS)

        draw()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()