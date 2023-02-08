import copy
import sys
# spread
# 
in_d = sys.stdin.readline
n,m = list(map(int, in_d().split()))
dat = [list(map(int, in_d().split())) for _ in range(n)]

max_anjeon = 0
zeros = 0
for y in range(n):
    for x in range(m):
        if dat[y][x] == 0:
            zeros += 1
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def checker(c):
    global max_anjeon, zeros
    if zeros - c < max_anjeon:
        #print('max anjeon check ', zeros, ' ',c, '  ' ,max_anjeon)
        return False
    return True

def spread_bfs(y,x,mat,cnt):
    global dx, dy, n, m
    cnt_in = 0
    for kka in range(4):
        ny = y + dy[kka]
        nx = x + dx[kka]
        if 0 <= ny < n and 0 <= nx < m and mat[ny][nx] == 0:

            mat[ny][nx] = 2
            cnt_in += 1
            if checker(cnt+cnt_in):
                cnt_in += spread_bfs(ny,nx,mat,cnt+cnt_in)
    return cnt_in

def spread(mat):
    global n,m,dat,max_anjeon,zeros
    cnt = 3 # 0->2 갯수 벽포함
    for y in range(n):
        for x in range(m):
            if dat[y][x] == 2:
                cnt += spread_bfs(y,x,mat,cnt)

    max_anjeon = max(max_anjeon,zeros - cnt)

def mk_buek_bfs(b,bc,mat_w_b):
    global n, m, dat
    if b != 0:
        for y in range(n):
            for x in range(m):
                if bc[y][x] == False and dat[y][x] == 0:
                    bc[y][x] = True
                    bc_t = copy.deepcopy(bc)
                    mat = copy.deepcopy(mat_w_b)
                    mat[y][x] = 1
                    mk_buek_bfs(b-1,bc_t,mat)
    else:
        spread(mat_w_b)

def run():
    global n,m,dat
    bc = [[False for x in range(m)] for y in range(n)]
    mat_w_b = [dat[y][:] for y in range(n)]
    mk_buek_bfs(3,bc,mat_w_b)



run()
print(max_anjeon)