f = open("./input.txt")


def solution():
    input = f.read()
    n = input.splitlines()
    ranges = []
    # find the ""
    index = n.index("")

    ranges = [tuple(map(int, s.split("-"))) for s in n[0:index]]
    ranges.sort()
    merged = []

    for start, end in ranges:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    merged = [tuple(r) for r in merged]
    res = 0
    for s, e in merged:
        res += (e - s) + 1
    return res


print(solution())
