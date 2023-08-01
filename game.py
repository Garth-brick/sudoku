from grid import Grid
from color import Color
import pygame


class Game:
    THIN_LINE_WIDTH = 2
    THICK_LINE_WIDTH = THIN_LINE_WIDTH * 3
    CELL_WIDTH = 60
    CELL_HEIGHT = CELL_WIDTH
    PADDING = 20
    WIDTH = CELL_WIDTH * 9 + THIN_LINE_WIDTH * 6 + THICK_LINE_WIDTH * 4 + PADDING * 2
    HEIGHT = WIDTH
    
    def __init__(self, width: float = WIDTH, height: float = HEIGHT):
        self.gameGrid: Grid = Grid()
        self.errorCount: int = 0
        self.width = width
        self.height = height
        self.gameScreen: pygame.Surface = pygame.Surface((self.width, self.height))
        self.numberFont: pygame.font.Font = pygame.font.Font("Times", 20)
    
    # handles tthe click events
    def handleMouseDown(self):
        pass
    
    # draws all the vertical and horizontal lines onto the gameScreen
    def drawLines(self):
        
        # initialising variables for the vertical lines 
        verticalLinesX = Game.PADDING
        verticalLinesStartY = Game.PADDING
        verticalLinesEndY = self.height - Game.PADDING
        
        # initialising variables for the horizontal lines 
        horizontalLinesY = Game.PADDING
        horizontalLinesStartX = Game.PADDING
        horizontalLinesEndX = self.width - Game.PADDING
        
        # we need to draw 10 lines on both axes (8 inside and 2 for borders)
        for i in range(0, self.gameGrid.COLS + 1):
            if i % 3:
                lineWidth = Game.THIN_LINE_WIDTH
            else:
                lineWidth = Game.THICK_LINE_WIDTH
                
            pygame.draw.rect(
                self.gameScreen,
                Color.LIGHT_GRAY,
                (verticalLinesX, verticalLinesStartY, lineWidth, verticalLinesEndY - verticalLinesStartY)
            )
            pygame.draw.rect(
                self.gameScreen,
                Color.LIGHT_GRAY,
                (horizontalLinesStartX, horizontalLinesY, horizontalLinesEndX - horizontalLinesStartX, lineWidth)
            )
            print(f"{verticalLinesX=}, {horizontalLinesY=}")
            
            horizontalLinesY += Game.CELL_HEIGHT + lineWidth
            verticalLinesX += Game.CELL_WIDTH + lineWidth
    
    # draws the values of the gameGrid onto the gameScreen
    def drawNumbers(self):
        pass
    
    # 'screen' - the surface on which we will blit the gameScreen after drawing on the gameScreen
    # 'position' - the (x, y) coordinates of the top-left corner of the gameScreen relative to the top-left of 'screen'
    count = 0
    def draw(self, screen: pygame.Surface, position: tuple[int, int]):
        
        # TESTING
        if Game.count > 0:
            return
        Game.count += 1
        # TESTING
        
        self.gameScreen.fill(Color.WHITE)
        self.drawLines()
        self.drawNumbers()
        screen.blit(self.gameScreen, position)