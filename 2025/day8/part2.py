f = open("input.txt")
import math
from collections import defaultdict


input = f.read().splitlines()


p = []
for line in input:
    x, y, z = [int(x) for x in line.split(",")]
    p.append((x, y, z))

D = []
for i, (x1, y1, z1) in enumerate(p):
    for j, (x2, y2, z2) in enumerate(p):
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        if i > j:
            D.append((dist, i, j))

UF = {i: i for i in range(len(p))}


def find(x):
    if x == UF[x]:
        return x
    UF[x] = find(UF[x])
    return UF[x]


def mix(x, y):
    UF[find(x)] = find(y)


D = sorted(D)
connections = 0
for _d, i, j in D:
    if find(i) != find(j):
        connections += 1
        if connections == len(p) - 1:
            print(p[i][0] * p[j][0])
    mix(i, j)

SZ = defaultdict(int)
for x in range(len(p)):
    SZ[find(x)] += 1

S = sorted(SZ.values())
# print(S[-1] * S[-2] * S[-3])
