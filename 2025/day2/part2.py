f = open("./input.txt")

"""
seperate ids by ,
ranges so 11 - 22,
11,12,13,14,15,16...20,21,22
95,96,97,98,99
find the sequence of digits repeated at least twice 

"""


def find_repeating_pattern(s):
    n = len(s)

    longest_prefix = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = longest_prefix[j - 1]
        if s[i] == s[j]:
            j += 1
            longest_prefix[i] = j

    last = longest_prefix[-1]
    repeat_len = n - last

    if last > 0 and n % repeat_len == 0:
        return s

    return None


def find_invalid(start, end):
    out = []
    for n in range(start, end + 1):
        s = str(n)

        val = find_repeating_pattern(s)

        if not val:
            continue

        out.append(int(val))

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
