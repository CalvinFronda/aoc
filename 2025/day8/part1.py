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

for _d, i, j in D[:1000]:
    mix(i, j)

SZ = defaultdict(int)
for x in range(len(p)):
    SZ[find(x)] += 1

S = sorted(SZ.values())
print(S[-1] * S[-2] * S[-3])


# print(len(input))
# p1 = [162, 817, 812]
# p2 = [425, 690, 689]
# p3 = [431, 825, 988]
# p2 = [431, 825, 988]
# print("start", p1)
# print("first", get_distance(p1, p2))
# print("second", get_distance(p1, p3))
# p4 = [906, 360, 560]
# p5 = [805, 96, 715]
# print("third", get_distance(p4, p5))


"""
keep track of circuit, there can be multiple that are closest 
Loop through and remove jBox that are connected
keep track of what was removed 


162,817,812 = 20

jbox = 

[
(0, '162,817,812'), 
(1, '57,618,57'), 
(2, '906,360,560'), 
(3, '592,479,940'), 
(4, '352,342,300'), 
(5, '466,668,158'), 
(6, '542,29,236'), 
(7, '431,825,988'), 
(8, '739,650,466'), 
(9, '52,470,668'), 
(10, '216,146,977'), 
(11, '819,987,18'), 
(12, '117,168,530'), 
(13, '805,96,715'), 
(14, '346,949,466'), 
(15, '970,615,88'), 
(16, '941,993,340'), 
(17, '862,61,35'), 
(18, '984,92,344'), 
(19, '425,690,689')]

2,13

[
((162, 817, 812), (425, 690, 689)), ((162, 817, 812), (431, 825, 988)), ((906, 360, 560), (805, 96, 715)), ((431, 825, 988), (425, 690, 689)), ((862, 61, 35), (984, 92, 344)), ((52, 470, 668), (117, 168, 530)), ((819, 987, 18), (941, 993, 340)), ((906, 360, 560), (739, 650, 466)), ((346, 949, 466), (425, 690, 689)), ((906, 360, 560), (984, 92, 344))]


"""
