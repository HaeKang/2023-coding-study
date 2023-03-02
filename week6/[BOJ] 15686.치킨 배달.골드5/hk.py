import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

homes = []
chickens = []


for i in range(n):
    r = list(map(int, input().split()))
    for j in range(n):
        if r[j] == 1:
            homes.append((i, j))
        elif r[j] == 2:
            chickens.append((i, j))

ans = 1e9
for com in combinations(chickens, m):
    dist = 0
    for home in homes:
        home_dist = 1e9
        for c in com:
            home_dist = min(home_dist, abs(
                home[0] - c[0]) + abs(home[1] - c[1]))
        dist += home_dist
        if dist > ans:
            break
    ans = min(ans, dist)

print(ans)
