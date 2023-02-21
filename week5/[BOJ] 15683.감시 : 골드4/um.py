import copy
import sys
from collections import Counter

in_d = sys.stdin.readline
N,M = list(map(int,in_d().split()))
mat = [list(map(int,in_d().split())) for _ in range(N)]
cctvs = list()
zeros = 0
for y in range(N):
    for x in range(M):
        val = mat[y][x]
        if val == 0:
            zeros += 1
        if val == 6:
            mat[y][x] = -1
        if 0 < val < 6:
            cctvs.append([val,y,x])
res = zeros
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def cc(n,y,x,mat,dir):
    global dx,dy
    cnt = 0
    for kka in range(7):
        ny = y + dy[dir] * (kka+1)
        nx = x + dx[dir] * (kka+1)
        if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] >= 0:
            if mat[ny][nx] == 0:  # 이미 바꾼거
                mat[ny][nx] = 6
                cnt += 1
        else :
            break
    if n == 3 or n == 4 or n == 5:
        for kka in range(7):
            ndir = (dir + 1) % 4
            ny = y + dy[ndir] * (kka+1)
            nx = x + dx[ndir] * (kka+1)
            if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] >= 0:
                if mat[ny][nx] == 0:  # 이미 바꾼거
                    mat[ny][nx] = 6
                    cnt += 1
            else:
                break
    if n == 2 or n == 4 or n == 5:
        for kka in range(7):
            ny = y + -dy[dir] * (kka+1)
            nx = x + -dx[dir] * (kka+1)
            if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] >= 0:
                if mat[ny][nx] == 0:  # 이미 바꾼거
                    mat[ny][nx] = 6
                    cnt += 1
            else:
                break
    if n == 5:
        for kka in range(7):
            ny = y + dy[dir - 1] * (kka+1)
            nx = x + dx[dir - 1] * (kka+1)
            if 0 <= ny < N and 0 <= nx < M and mat[ny][nx] >= 0:
                if mat[ny][nx] == 0:  # 이미 바꾼거
                    mat[ny][nx] = 6
                    cnt += 1
            else:
                break
    return cnt

def bfs(idx,mat,cnt):
    global cctvs,res
    if idx == len(cctvs):
        #print(zeros,cnt,res,idx)
        res = min(zeros-cnt,res)
        return
    n,y,x = cctvs[idx]
    if n == 1 or n == 3 or n == 4:
        for kka in range(4):
            nmat = copy.deepcopy(mat)
            ncnt = cnt + cc(n,y,x,nmat,kka)
            bfs(idx+1,nmat,ncnt)
    elif n == 2:
        for kka in range(2):
            nmat = copy.deepcopy(mat)
            ncnt = cnt + cc(n,y,x,nmat,kka)
            bfs(idx+1,nmat,ncnt)
    else:
        nmat = copy.deepcopy(mat)
        ncnt = cnt + cc(n, y, x, nmat, 0)
        bfs(idx + 1, nmat, ncnt)

bfs(0,mat,0)
print(res)