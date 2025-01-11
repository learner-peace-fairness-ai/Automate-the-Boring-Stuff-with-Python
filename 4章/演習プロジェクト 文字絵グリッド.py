# 2次元リストの文字を縦横を逆転して表示する

def print_grid_horizontally_and_vertically_inverted(grid):
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])

    for ci in range(MAX_COLUMN):
        for ri in range(MAX_ROW):
            print(grid[ri][ci], end='')

        print()


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.']]

print_grid_horizontally_and_vertically_inverted(grid)
