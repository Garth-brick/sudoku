# import pygame
# from color import Color


class Grid:
    ROWS: int = 9
    COLS: int = 9
    COLS_PER_BOX: int = COLS // 3
    ROWS_PER_BOX: int = ROWS // 3
    SENTINEL: int = 0
    VALUES: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8, 9)


    def __init__(self, grid: list[list[int]]=[]) -> None:
        self.grid: list[list[int]] = [[Grid.SENTINEL] * Grid.COLS for _ in range(Grid.ROWS)]
        self.pencil_grid: list[list[set[int]]] = [[set() for _ in range(Grid.COLS)] for _ in range(Grid.ROWS)]
        self._rowValues: list[set[int]] = [set() for _ in range(Grid.ROWS)]
        self._colValues: list[set[int]] = [set() for _ in range(Grid.COLS)]
        self._boxValues: list[set[int]] = [set() for _ in range(Grid.COLS)]
        if grid:
            self._initialiseBoard(grid)


    def __repr__(self) -> str:
        result: list[str] = []
        for row in range(Grid.ROWS):
            if row > 0 and row % 3 == 0:
                #               1  2  3 | 4  5  6 | 7  8  9
                result.append("---------+---------+---------")
                #               1  2  3 | 4  5  6 | 7  8  9
            resultRow = []
            for col in range(Grid.COLS):
                if col > 0 and col % 3 == 0:
                    resultRow.append("|")
                if self.grid[row][col] == 0:
                    resultRow.append("   ")
                else:
                    resultRow.append(f" {self.grid[row][col]} ")
            result.append("".join(resultRow))
        return "\n".join(result)


    def _initialiseBoard(self, grid: list[list[int]]) -> None:
        assert len(grid) == Grid.ROWS, "incorrect number of rows in input"
        for row in grid:
            assert len(row) == Grid.COLS, "incorrect number of columns in input"
        
        for row in range(Grid.ROWS):
            for col in range(Grid.COLS):
                value: int = grid[row][col]
                self.grid[row][col] = value
                if not value:
                    continue
                # isInRow[row] is a set containing all the values in that row
                
                # checking if the board being created is actually valid before creating it
                boxNum: int = Grid.getBoxNum(row, col)
                assert (value not in self._rowValues[row] | 
                        self._colValues[col] | 
                        self._boxValues[boxNum]), "unsolvable board created"
                
                self.setGridValue(row, col, value)


    def _getNextEmptyCellCoordinates(self) -> tuple[int, int] | None:
        for row in range(Grid.ROWS):
            for col in range(Grid.COLS):
                if self.grid[row][col] == 0:
                    return (row, col)
        return None

    @staticmethod
    def getBoxNum(row: int, col: int) -> int:
        return (row // 3) * 3 + (col // 3)


    def isValidAssignment(self, row: int, col: int, value: int) -> bool:
        boxNum = Grid.getBoxNum(row, col)
        return (row in range(Grid.ROWS) and col in range(Grid.COLS) and 
                value in range(1, len(Grid.VALUES) + 1) and
                value not in (self._rowValues[row] | self._colValues[col] |
                              self._boxValues[boxNum]))


    def _resetGridValue(self, row: int, col: int) -> None:
        value: int = self.grid[row][col]
        
        if value == Grid.SENTINEL:
            # if the value was already null then return
            return
        
        # removing the value from the grid
        self.grid[row][col] = Grid.SENTINEL
        
        # removing the value from the 
        boxNum: int = Grid.getBoxNum(row, col)
        self._rowValues[row].discard(value)
        self._colValues[col].discard(value)
        self._boxValues[boxNum].discard(value)


    def setGridValue(self, row: int, col: int, value: int) -> None:
        assert self.isValidAssignment(row, col, value), "invalid assignment"
        
        self.grid[row][col] = value
        boxNum: int = Grid.getBoxNum(row, col)
        self._rowValues[row].add(value)
        self._colValues[col].add(value)
        self._boxValues[boxNum].add(value)


    def updatePencilValue(self, row: int, col: int, value: int) -> None:
        assert (row in range(Grid.ROWS) and col in range(Grid.COLS) and
                value in range(1, len(Grid.VALUES) + 1)), "invalid assignment"
        
        if value in self.pencil_grid[row][col]:
            # if this number was already present then remove it from the set
            self.pencil_grid[row][col].remove(value)
        else:
            # if this number was not present then add it to the set
            self.pencil_grid[row][col].add(value)


    def resetPencilValue(self, row: int, col: int) -> None:
        assert (row in range(Grid.ROWS) and col in range(Grid.COLS)), "invalid coordinates"
        self.pencil_grid[row][col].clear()


    def solve(self) -> bool:
        nextEmptyCell: tuple[int, int] | None = self._getNextEmptyCellCoordinates()
        if not nextEmptyCell:
            # if all cells have been filled and no empty cells then solving is complete
            return True
        
        # if there is an empty cell then unpack it
        row, col = nextEmptyCell
        
        for value in Grid.VALUES:
            # loop through all the possible values
            if not self.isValidAssignment(row, col, value):
                continue
            
            # if we can assing a value to this empty cell then assign it
            self.setGridValue(row, col, value)
            
            # now check for the remaining board
            if self.solve():
                return True
            
            # if the rest of the board was not solvable then undo this assignment
            self._resetGridValue(row, col)
                
        # if none of the values worked out then 
        return False
