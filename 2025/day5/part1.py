f = open("./input.txt")


def solution():
    input = f.read()
    n = input.splitlines()
    ranges = []
    # find the ""
    index = n.index("")
    foods = n[index + 1 :]
    ranges = [tuple(map(int, s.split("-"))) for s in n[0:index]]
    result = 0
    seen = []
    # for every value in food
    for start, end in ranges:
        for food in foods:
            # check if they fall within the range for each value
            if food in seen:
                continue
            if start <= int(food) <= end:
                seen.append(food)
                result += 1

    return result


print(solution())
