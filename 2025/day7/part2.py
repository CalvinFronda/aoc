f = open("./input.txt")

from functools import cache


input = f.read()
grid = [list(row) for row in input.splitlines()]

rows = len(grid)
cols = len(grid[0])


def solution():
    @cache
    def counter(r, c):
        if r + 1 == rows:
            return 1
        if grid[r + 1][c] == "^":
            return counter(r + 1, c - 1) + counter(r + 1, c + 1)
        else:
            return counter(r + 1, c)

    start_col = grid[0].index("S")

    count = counter(0, start_col)

    return count


print(solution())
