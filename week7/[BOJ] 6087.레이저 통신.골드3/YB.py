m, n = map(int, input().split())
arr = []
cxy = []
for i in range(n):
    arr.append(input())
    for j in range(m):
        if arr[i][j] == 'C':
            cxy.append([i, j])

#방향을 몇번 바꿔야하는가!
answer = float('inf')

dx = [1, 0, -1, 0] # 아래 오른 왼 위
dy = [0, 1, 0, -1]

from collections import deque
costs = [[float('inf')]*m for _ in range(n)]
cx, cy = cxy[0]
ox, oy = cxy[-1]
costs[cx][cy] = 0

q = deque()
for d in range(4):
    q.append([cx, cy, d, 0])

while q:
    x, y, d, cnt = q.popleft()
    if costs[x][y] < cnt:
        continue
    if x == ox and y == oy:
        answer = min(answer, cnt)
        continue

    for nd in range(4):
        nx, ny = x+dx[nd], y+dy[nd]
        if not (0<= nx < n and 0<= ny < m) or arr[nx][ny] == '*':
            continue
        if d == nd and costs[nx][ny] > cnt: # 거울 추가 x -> d로 한칸
            costs[nx][ny] = cnt
            q.append([nx, ny, d, cnt])
        elif d != nd and costs[nx][ny] >= cnt+1: # 거울 추가 -> 다른 방향으로 한칸
            costs[nx][ny] = cnt+1
            q.append([nx, ny, nd, cnt+1])

costs = [[float('inf')] * m for _ in range(n)]
cx, cy = cxy[-1]
ox, oy = cxy[0]
costs[cx][cy] = 0

q = deque()
for d in range(4):
    q.append([cx, cy, d, 0])

while q:
    x, y, d, cnt = q.popleft()
    if costs[x][y] < cnt:
        continue
    if x == ox and y == oy:
        answer = min(answer, cnt)
        continue

    for nd in range(4):
        nx, ny = x + dx[nd], y + dy[nd]
        if not (0 <= nx < n and 0 <= ny < m) or arr[nx][ny] == '*':
            continue
        if d == nd and costs[nx][ny] > cnt:  # 거울 추가 x -> d로 한칸
            costs[nx][ny] = cnt
            q.append([nx, ny, d, cnt])
        elif d != nd and costs[nx][ny] >= cnt + 1:  # 거울 추가 -> 다른 방향으로 한칸
            costs[nx][ny] = cnt + 1
            q.append([nx, ny, nd, cnt + 1])

print(answer)
