f = open("input.txt")


def solution():
    input = f.read()
    cleaned = input.split("\n")
    res = 0

    for bank in cleaned:
        curr_max = 0

        for i in range(len(bank)):
            for j in range(1, len(bank)):
                if i < j:
                    val = int(bank[i] + bank[j])
                    curr_max = max(curr_max, val)

        res += curr_max
    return res


print(solution())
