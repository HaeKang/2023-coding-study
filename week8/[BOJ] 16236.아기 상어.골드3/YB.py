# n, n 크기, 물고기 M마리 아기상어 1마리

#
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    if 9 in arr[i]:
        for j in range(n):
            if arr[i][j] == 9:
                sx, sy = i, j
arr[sx][sy] = float('inf')

ss = 2

from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def find_fish(x, y):
    global ss
    # 아기상어 크기 2, 1초에 상하좌우 한칸 이동
    # 자기보다 크기 큰 물고기 있는 칸 지나갈 수 x, 나머지 가능
    # 자기보다 크기 작은 물고기만 먹을 수 o
    # 크기 같으면: 물고기 못먹고, 지나가는 건 가능
    q = deque()
    visited = [[False]*n for _ in range(n)]
    q.append([x, y, 0])
    visited[x][y] = True
    fishs = []
    dist = n*n+1
    # 상어 이동방향 결정
    # 1. 더이상 먹을 수 있는 물고기 없으면 도움 요청
    # 2. 먹을 수 있는 물고기 1마리면, 그쪽 감
    #  1마리보다 많으면 거리 가장 가장 가까운 물고기
    #  거리 가까운 물고기 많으면 x작은> y작은 순으로
    while q:
        x, y, cnt = q.popleft()
        if cnt == dist and 0< arr[x][y] < ss:
            fishs.append([x, y])
        elif cnt < dist and 0< arr[x][y] < ss:
            fishs = [[x, y]]
            dist = cnt
        elif cnt > dist:
            continue
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if not (0<= nx < n) or not (0<= ny < n) or visited[nx][ny] or arr[nx][ny] > ss:
                continue
            visited[nx][ny] = True
            q.append([nx, ny, cnt+1])
    if fishs:
        fishs.sort()
        return fishs[0][0], fishs[0][1], dist
    else:
        return -1, -1, -1
    # 상어 크기 업뎃: 상어 크기랑 같은 물고기 1마리 먹을 때 크기가 1 증가


# 도움 요청까지 몇초동안 물고기 먹는지
t = 0
eat_fish = 0
while True:
    fx, fy, dist = find_fish(sx, sy)
    if dist == -1:
        break

    eat_fish += 1

    if eat_fish == ss:
        eat_fish = 0
        ss += 1

    arr[fx][fy] = float('inf')
    arr[sx][sy] = 0
    sx, sy = fx, fy
    t += dist
print(t)
