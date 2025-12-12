f = open("sample.txt")


def move(index, step):
    return (index + step) % 100


def solution():
    read = f.read()
    zero_count = 0
    curr_idx = 50
    input = [line for line in read.splitlines() if line]

    for s in input:
        dir = s[0]
        step = int(s[1:])

        if dir == "L":
            curr_idx = move(curr_idx, -step)
            if curr_idx == 0:
                zero_count += 1
        else:
            curr_idx = move(curr_idx, step)
            if curr_idx == 0:
                zero_count += 1

    return zero_count


print(solution())
