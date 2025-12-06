f = open("./sample.txt")


def search(grid, r, c):
    word = "XMAS"
    rows = len(grid)
    cols = len(grid[0])

    # must match first letter
    if grid[r][c] != word[0]:
        return False

    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1),  # right
        (-1, -1),  # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1),  # down-right
    ]

    # check each direction
    for dr, dc in directions:
        match = True
        for i in range(len(word)):
            nr = r + dr * i
            nc = c + dc * i

            # out of bounds? direction fails
            if not (0 <= nr < rows and 0 <= nc < cols):
                match = False
                break

            if grid[nr][nc] != word[i]:
                match = False
                break

        if match:
            return True

    return False


def solution():
    grid = [list(line) for line in f.read().splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    res = 0

    for row in range(rows):
        for col in range(cols):
            if search(grid, row, col):
                res += 1

    return res


print(solution())
