import sys
from collections import deque

in_d = sys.stdin.readline
N = int(in_d())
mat = [list(map(int, in_d().split())) for _ in range(N)]

smat = [[[0,0,0] for kka in range(N)] for _ in range(N)] # 가 세 대
smat[0][1] = [1,0,0]
mat[0][0], mat[0][1] = 2, 2
dx = [1,0]
dy = [0,1]

Q = deque([(0,1)])
while Q:
    y,x = Q.popleft()
    for i in range(2):
        ny, nx = y + dy[i] , x + dx[i]
        if (not (0 <= ny < N and 1 <= nx < N)) or mat[ny][nx] > 0:
            continue
        # 해당 위치 에서
        # 가로로 있을수 있는 경우
        if 0 <= ny < N and 1 <= nx - 1 < N and mat[ny][nx-1] != 1:
            smat[ny][nx][0] = smat[ny][nx-1][0] + smat[ny][nx-1][2]
        # 세로로 있을수 잇는 경우
        if 0 <= ny - 1 < N and 1 <= nx < N and mat[ny-1][nx] != 1:
            smat[ny][nx][1] = smat[ny-1][nx][1] + smat[ny-1][nx][2]
        # 대각선으로 있을 수 잇는 경우
        if 0 <= ny - 1 < N and 1 <= nx - 1 < N and mat[ny-1][nx-1] != 1 and mat[ny][nx-1] != 1 and mat[ny-1][nx] != 1:
            smat[ny][nx][2] = sum(smat[ny-1][nx-1])

        mat[ny][nx] = 2
        Q.append((ny,nx))

print(sum(smat[N-1][N-1]))