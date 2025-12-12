f = open("./input.txt")

from collections import deque

input = f.read()
grid = [list(row) for row in input.splitlines()]

rows = len(grid)
cols = len(grid[0])


def solution():
    sr = 0
    sc = grid[sr].index("S")
    que = deque([(sr, sc)])

    count = 0
    seen = set()
    while que:
        r, c = que.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if r + 1 == rows:
            continue
        if grid[r + 1][c] == "^":
            que.append((r + 1, c - 1))
            que.append((r + 1, c + 1))
            count += 1
        else:
            que.append((r + 1, c))

    return count


print(solution())
