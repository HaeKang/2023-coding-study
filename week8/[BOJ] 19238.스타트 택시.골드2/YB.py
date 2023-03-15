# m번 반복

# 승객 고를 때는 가장 가까운 곳 > 행 작은 > 열 작은
# 한칸 이동 > 연료 1만큼 소모
# 목적지 이동 완료 > 소모한 연료양 *2

# 이동하다가 연료 바닥나면 시래, 끝
# 도착했을 때의 연료 0인 건 ㄱㅊ

# 남은 연료양/ 이동 불가능하면 -1 출력


n, m, fuel = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

tx, ty = map(int, input().split())
tx, ty = tx-1, ty-1

psg = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    sx, sy, ox, oy = map(int, input().split())
    psg[sx-1][sy-1] = [ox-1, oy-1]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

from collections import deque
def find_psg():
    global tx, ty
    q = deque()
    q.append([tx, ty, 0])
    min_dist_psg = []
    min_dist = float('inf')
    visited = [[False]*n for _ in range(n)]
    visited[tx][ty] = True
    while q:
        x, y, cnt = q.popleft()
        if psg[x][y]:
            if cnt < min_dist:
                min_dist_psg = [[x, y]]
                min_dist = cnt

            elif cnt == min_dist:
                min_dist_psg.append([x, y])

        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if not (0<= nx < n and  0<= ny < n) or visited[nx][ny] or arr[nx][ny] == 1:
                continue
            visited[nx][ny] = True
            q.append([nx, ny, cnt+1])
    min_dist_psg.sort()
    if min_dist_psg:
        return min_dist_psg[0][0], min_dist_psg[0][1], min_dist
    else:
        return -1, -1, -1

def cal_dest(sx, sy, ox, oy):
    q = deque()
    q.append([sx, sy, 0])
    visited = [[False] * n for _ in range(n)]
    visited[sx][sy] = True
    while q:
        x, y, cnt = q.popleft()
        if x == ox and y == oy:
            return cnt
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if not (0<= nx < n and 0<= ny < n) or visited[nx][ny] or arr[nx][ny]:
                continue
            visited[nx][ny] = True
            q.append([nx, ny, cnt+1])
    return -1

for _ in range(m):
    px, py, pickup = find_psg()
    if pickup == -1:
        fuel = -1
        break
    if fuel < pickup:
        fuel = -1
        break

    fuel -= pickup
    ox, oy = psg[px][py]

    dropoff = cal_dest(px, py, ox, oy)
    psg[px][py] = []

    if dropoff == -1:
        fuel = -1
        break

    if fuel < dropoff:
        fuel = -1
        break

    fuel += dropoff
    tx, ty = ox, oy

print(fuel)
