import sys
from itertools import combinations

in_d = sys.stdin.readline
N,M = list(map(int,in_d().split()))
mat = [list(map(int,in_d().split())) for _ in range(N)]
res = 1e6
chic, zip = list(), list()
zipd = list()
for y in range(N):
    for x in range(N):
        if mat[y][x] == 2:
            chic.append((y,x))
        if mat[y][x] == 1:
            zip.append((y,x))
chic_getsu = len(chic)

comb = combinations(chic,M)
for com in comb:
    td = 0
    for zy,zx in zip:
        val = 10000
        for cy,cx in com:
            d = abs(cy-zy) + abs(cx-zx)
            val = min(d,val)
        td += val
        if td >= res:
            break
    res = min(res,td)

print(res)