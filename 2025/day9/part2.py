f = open("sample.txt")


input = f.read().splitlines()
input = [list(map(int, x.split(","))) for x in input]

col_max = [(lambda col: max(col))(c) for c in zip(*input)]


res = -1

# get the max area w * h
# 1 7

# if the x's are same
# everything from y1-y2 is a col boundry

# if the y's are the same
# everything from x1-x2 is a row boundy

boundaries = set()

for i, (x, y) in enumerate(input):
    curr = [x, y]

    for j in range(len(input)):
        if i == j:
            continue
        check = input[j]
        # if x's are the same
        if curr[0] == check[0]:
            y_start, y_end = sorted([curr[1], check[1]])
            for ys in range(y_start, y_end + 1):
                boundaries.add((check[0], ys))
                continue
        # if y's are the same
        if curr[1] == check[1]:
            x_start, x_end = sorted([curr[0], check[0]])
            for xs in range(x_start, x_end + 1):
                boundaries.add((xs, check[1]))
                continue

x_hash = {}

# print("x", col_max[0])
# print("y", col_max[1])

for x, y in boundaries:
    if x not in x_hash:
        x_hash[x] = [float("inf"), float("-inf")]
    x_hash[x] = [min(y, x_hash[x][0]), max(y, x_hash[x][1])]


# print(x_hash)


"""
hashmap is 

col : [col, row]
"""


# get the max area w * h
for i, (x, y) in enumerate(input):
    curr = [x, y]
    curr_idx = input.index(curr)
    for j in range(len(input)):
        if curr_idx == j:
            continue
        check = input[j]

        # find abs diff of x and y
        # these are diag
        # [7,3]
        # [11,1]
        # 7,1
        # 11, 3
        p1 = curr
        p2 = check
        p3 = (p1[0], p2[1])
        p4 = (p2[0], p1[1])

        if p3[0] not in x_hash:
            continue

        if p4[0] not in x_hash:
            continue

        min1, max1 = x_hash[p3[0]]
        min2, max2 = x_hash[p4[0]]

        if not (min1 <= p3[1] and p3[1] <= max1):
            continue

        if not (min2 <= p4[1] and p4[1] <= max2):
            continue
        # if p3[1] in within the range of x_hash[p3[0]]

        diff = (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

        res = max(res, diff)

print(res)

# 4604141472 too high
