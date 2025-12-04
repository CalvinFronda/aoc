"""
Think of everything as an grid
each coordinate should check 8 positions
keep count of if we see an @ sign
if there are fewer than 4 that we see, we can increment a counter

"""

sample = "./sample.txt"
real = "./input.txt"
f = open(real)


def solution():
    intake = f.read()
    grid = []

    for line in intake.splitlines():
        if line.strip() == "":
            continue
        grid.append(list(line))

    dirs = [
        (-1, 0),  # top
        (-1, 1),  # top-right
        (0, 1),  # right
        (1, 1),  # bottom-right
        (1, 0),  # bottom
        (1, -1),  # bottom-left
        (0, -1),  # left
        (-1, -1),  # top-left
    ]

    rows = len(grid)
    cols = len(grid[0])
    res = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != "@":
                continue
            count = 0

            # run each dir on a cell
            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        count += 1

                if count >= 4:
                    break

            else:
                if count <= 4:
                    res += 1

    return res


print(solution())
