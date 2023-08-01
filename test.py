from grid import Grid


grid_input: list[list[int]] = [[] for _ in range(9)]
for row in range(9):
    grid_input[row] = list(map(int, input().strip().split()))

game_grid = Grid(grid_input)
print(game_grid._rowValues)

print(game_grid)

game_grid.solve()
print("\nSOLVED: \n")
print(game_grid)

"""input
7 8 0 4 0 0 1 2 0
6 0 0 0 7 5 0 0 9
0 0 0 6 0 1 0 7 8
0 0 7 0 4 0 2 6 0
0 0 1 0 5 0 9 3 0
9 0 4 0 6 0 0 0 5
0 7 0 3 0 0 0 1 2
1 2 0 0 0 7 4 0 0
0 4 9 2 0 6 0 0 7
"""