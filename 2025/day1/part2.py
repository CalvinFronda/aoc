f = open("input.txt")


def move(index, step):
    return (index + step) % 100


def times_seen_zero(curr_idx, step, dir):
    SIZE = 100

    if dir == "L":
        first = curr_idx % SIZE
    else:
        first = (SIZE - (curr_idx % SIZE)) % SIZE

    if first == 0:
        first = SIZE

    if first > step:
        return 0

    return (step - first) // SIZE + 1


def solution():
    read = f.read()

    zero_count = 0
    curr_idx = 50
    input = [line for line in read.splitlines() if line]

    for s in input:
        dir = s[0]
        step = int(s[1:])

        zero_count += times_seen_zero(curr_idx, step, dir)
        delta = -step if dir == "L" else step
        curr_idx = move(curr_idx, delta)

    return zero_count


print(solution())
