import sys
from collections import deque

in_d = sys.stdin.readline
N = int(in_d())
mat = [list(map(int, in_d().split())) for _ in range(N)]
as_size = 2
mul = list()
sty,stx = 0,0
for y in range(N):
    for x in range(N):
        if mat[y][x] == 9:
            sty,stx = y,x
            mat[y][x] = 0
        if 1 <= mat[y][x] <= 6:
            mul.append((y,x,mat[y][x]))
dy = [-1,0,1,0]
dx = [0,-1,0,1]
t = 0

def go_mul(y,x,mul):
    global as_size, t, mat, dy, dx, N
    d = 50
    nmat = [[d] * N for _ in range(N)]
    slist = list()
    nmat[y][x] = 999
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if (not (0 <= ny < N and 0 <= nx < N)) or mat[ny][nx] > as_size:
            continue
        nmat[ny][nx] = 1
        for ii in range(2):
            iii = ( i + ii ) % 4
            nny, nnx = ny + dy[iii], nx + dx[iii]
            if (not (0 <= nny < N and 0 <= nnx < N)) or mat[nny][nnx] > as_size:
                continue
            slist.append((nny,nnx))
    dm,dm_n = 0, 1
    Q = deque(slist)
    while Q:
        ny, nx = Q.popleft()
        if (not (0 <= ny < N and 0 <= nx < N)) or mat[ny][nx] > as_size:
            continue
        d_list = list()
        for i in range(4):
            nny, nnx = ny + dy[i], nx + dx[i]
            if (not (0 <= nny < N and 0 <= nnx < N)) or mat[nny][nnx] > as_size:
                continue
            d_list.append(nmat[nny][nnx] + 1)
        d = min(d_list)
        if nmat[ny][nx] > d:
            nmat[ny][nx] = d
        for i in range(4):
            nny, nnx = ny + dy[i], nx + dx[i]
            if (not (0 <= nny < N and 0 <= nnx < N)) or mat[nny][nnx] > as_size:
                continue
            if nmat[nny][nnx] - d >= 2:
                Q.append((nny,nnx))
        # for time
        dm = max(d, dm)
        if dm >= dm_n * N/2:
            ol = list()
            trig = True
            for kka in range(len(mul)):
                my, mx, ms = mul[kka]
                if as_size > ms:
                    ol.append((nmat[my][mx],my,mx,ms,kka))
                    trig = False
            if trig == False:
                return ol, trig, mul
            else:
                dm_n += 1

    return ol, trig, mul
def eat_mul(y,x):
    global t, mul, as_size, mat
    eat_cnt = 0
    while True:
        ol, trig, mul = go_mul(y,x,mul)
        if trig:
            break
        ol.sort()
        #print()
        #print(ol)
        d, y, x, ms, idx = ol[0]
        mat[y][x] = 0
        t += d
        eat_cnt += 1
        if eat_cnt == as_size:
            as_size += 1
            eat_cnt = 0
        del mul[idx]

    return t

print(eat_mul(sty,stx))