f = open("./sample.txt")


def add_helper(add_list):
    res = 0
    for val in add_list:
        res += val

    return res


def multiply_helper(multi_list):
    res = 1
    for val in multi_list:
        res *= val

    return res


def solution():
    r = f.read()
    input = r.splitlines("")
    input = [v.split() for v in input]

    rows = len(list(input))
    cols = len(list(input)[0])
    res = 0

    for col in range(cols):
        store = []
        for row in range(rows):
            value = input[row][col]

            if value == "+":
                res += add_helper(store)
                continue
            elif value == "*":
                res += multiply_helper(store)
                continue

            if value != "+" or value != "*":
                store.append(int(value))

    return res


print(solution())
