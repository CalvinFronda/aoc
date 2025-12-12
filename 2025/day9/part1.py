f = open("input.txt")

input = f.read().splitlines()
input = [list(map(int, x.split(","))) for x in input]

res = -1

# get the max area w * h
for i, (x, y) in enumerate(input):
    curr = [x, y]
    curr_idx = input.index(curr)
    for j in range(len(input)):
        if curr_idx == j:
            continue
        check = input[j]
        # if they are on the same x
        # subract the x's + 1
        if curr[0] == check[0]:
            val = abs(curr[1] - check[1]) + 1
            res = max(res, val)
            continue
        # if they are on the same y
        # subtract the y's + 1
        # 7,1 7,3
        if curr[1] == check[1]:
            val = abs(curr[0] - check[0]) + 1
            res = max(res, val)
            continue

        # find abs diff of x and y
        x1 = curr[0]
        x2 = check[0]

        y1 = curr[1]
        y2 = check[1]

        diff = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

        res = max(res, diff)
print(res)
