f = open("input.txt")
"""
find the largest number out of 12 ints


"""


def solution():
    input = f.read()
    cleaned = input.split("\n")
    K = 12
    res = []

    for bank in cleaned:
        drop = len(bank) - K
        stack = []

        for d in bank:
            while drop > 0 and stack and stack[-1] < d:
                stack.pop()
                drop -= 1
            stack.append(d)

        res.append("".join(stack[:K]))

    return sum(int(n) for n in res)


print(solution())
