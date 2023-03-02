import copy
from itertools import combinations
n, m = map(int, input().split())
arr = []
house, bhcs = [], []
for i in range(n):
    arr.append(list( map(int, input().split())))
    for j in range(n):
        if arr[i][j] == 2:
            bhcs.append([i, j])
            arr[i][j] = 0
        elif arr[i][j] == 1:
            house.append([i, j])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

comb_bhcs = combinations(bhcs, m)
answer = float('inf')

from collections import deque
def cal_dist(chicken, x, y):
    global new_arr, answer
    dist = float('inf')
    for cx, cy in chicken:
        dist = min(dist, abs(cx-x)+abs(cy-y))
    return dist

for bhcs in comb_bhcs:
    #도시거리 구하기
    temp = 0
    for x, y in house:
        temp += cal_dist(bhcs, x, y)
    answer = min(answer, temp)
print(answer)
