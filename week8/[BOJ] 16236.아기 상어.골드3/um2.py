import sys
from collections import deque

in_d = sys.stdin.readline
N = int(in_d())
mat = [list(map(int, in_d().split())) for _ in range(N)]
as_size = 2
mul = list() # 물고기 모음
sty,stx = 0,0
for y in range(N):
    for x in range(N):
        if mat[y][x] == 9:
            sty,stx = y,x # 시작위치
            mat[y][x] = 0
        if 1 <= mat[y][x] <= 6:
            mul.append((y,x,mat[y][x]))
dy = [-1,0,1,0]
dx = [0,-1,0,1]
t = 0

def go_mul(y,x):
    global as_size, t, mat, dy, dx, N
    d = -1
    nmat = [[d] * N for _ in range(N)] # -1 거리로 초기화
    nmat[y][x] = 0
    Q = deque([(y,x,0)])
    while Q:
        y, x, d = Q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (not (0 <= ny < N and 0 <= nx < N)) or mat[ny][nx] > as_size or nmat[ny][nx] != -1:
                continue # 갈수 있는 길 체크 / 최단거리 체크 했는지 체크
            nmat[ny][nx] = d + 1
            Q.append((ny, nx, d + 1))
        #print('==================')
        #for kka in range(N):
        #    print(nmat[kka])

    return nmat
def eat_mul(y,x):
    global t, mul, as_size, mat
    eat_cnt = 0
    while True:
        if len(mul) == 0:
            break
        nmat = go_mul(y,x)
        nm = list()
        for kka in range(len(mul)):
            ny, nx, ms = mul[kka]
            if nmat[ny][nx] >= 0: # 거리 소팅 편하기 위해
                if ms < as_size: # 물고기가 작아야 먹을 수 있음
                    nm.append((nmat[ny][nx], ny, nx, ms, kka))
        nm.sort()
        if len(nm) == 0: # 먹을수 있는 물고기 없음
            break
        #for kka in range(N):
        #    print(nmat[kka])
        d, y, x, ms, idx = nm[0] # 최단 거리 물고기
        #print('========-=-=-=-=-=-=-=-=-=',d,t)
        if d < 0:
            break
        mat[y][x] = 0 # 해당 물고기 지워줌
        t += d
        eat_cnt += 1
        if eat_cnt == as_size: # 먹은 물고기 수 체크
            as_size += 1
            eat_cnt = 0
        del mul[idx]

    return t
eat_mul(sty,stx)
print(t)