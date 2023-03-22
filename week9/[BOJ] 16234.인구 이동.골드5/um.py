import sys
from collections import deque

in_d = sys.stdin.readline
N, L, R = list(map(int, in_d().split()))
mat = [list(map(int, in_d().split())) for kka in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
t = 0

def find_yun(chk,yt):
    global dx, dy, mat, L, R
    Q = deque(yt)
    while Q:
        y, x = Q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (not (0 <= ny < N and 0 <= nx < N)) or chk[ny][nx]:
                continue
            if L <= abs(mat[y][x] - mat[ny][nx]) <= R:
                yt.append((ny,nx))
                Q.append((ny, nx))
                chk[ny][nx] = True

while 2000: # 최대값
    yuns = list()
    chk = [[False] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if chk[y][x] == False:
                chk[y][x] = True
                yt = [(y,x)] # 기준점
                find_yun(chk,yt) # 연합 집합 찾기
                if len(yt) > 1: # 기준점 포함하여 다른 국가가 조건 만족할때
                    yuns.append(yt)
    if len(yuns) == 0:
        break
    for kka in range(len(yuns)):
        getsu = len(yuns[kka])
        val = 0
        for kki in range(getsu):
            val += mat[yuns[kka][kki][0]][yuns[kka][kki][1]]
        val = int(val/getsu)
        for kki in range(getsu):
            mat[yuns[kka][kki][0]][yuns[kka][kki][1]] = val
    t += 1
print(t)