# seperate ids by ,
# ranges so 11 - 22,
# 11,12,13,14,15,16...20,21,22
# 95,96,97,98,99

f = open("./input.txt")


def find_invalid(start, end):
    out = []
    for n in range(start, end + 1):
        s = str(n)
        L = len(s)

        if L % 2 != 0:
            continue
        half = L // 2

        if s[:half] == s[half:]:
            out.append(n)

    return out


def solution():
    read = f.read()
    input = [line for line in read.split(",")]
    result = []

    for r in input:
        start, end = r.split("-")
        val = find_invalid(int(start), int(end))
        if val:
            result.append(val)

    final = 0

    for sub in result:
        for num in sub:
            final += num
    return final


print(solution())
