import copy
from collections import deque
import sys

N,M = map(int,sys.stdin.readline().rstrip().split())

area = []
for i in range(N):
    area.append(list(map(int,sys.stdin.readline().rstrip().split())))

zero_area = []
virus = []
for i in range(N):
    for j in range(M):
        if not(area[i][j]):
            zero_area.append((i,j))
        if area[i][j] == 2:
            virus.append((i,j))

selected = []
def select(): # 벽 3개 선택하는 dfs 로직
    global selected

    if len(selected) == 3: # 3개 선택했으면 bfs로 바이러스 퍼지는 것을 시뮬레이션
        copied = copy.deepcopy(area)
        for k in selected:
            i,j = zero_area[k]
            copied[i][j] = 1
        bfs(copied)
        return

    for k in range(len(zero_area)):
        if len(selected) == 0 or selected[-1] < k:
            selected.append(k)
            select()
            selected.pop()

max_cnt = 0
dy = [-1,1,0,0]
dx = [0,0,-1,1]
def bfs(copied_area):
    global max_cnt
    q = deque()

    for v in virus:
        q.append(v)

    while(q):
        current = q.popleft()
        y,x = current
        for i in range(4):
            next_y, next_x = y+dy[i], x+dx[i]
            if next_y >= N or next_x >= M or next_y < 0 or next_x < 0:
                continue
            if copied_area[next_y][next_x] == 0:
                q.append((next_y, next_x))
                copied_area[next_y][next_x] = 2

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not(copied_area[i][j]):
                cnt += 1
    max_cnt = max(cnt, max_cnt)

select()
print(max_cnt)