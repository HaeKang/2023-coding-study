import sys
from collections import Counter
# ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ
in_d = sys.stdin.readline
N,M,H = list(map(int,in_d().split()))
lad_in = [list(map(int,in_d().split())) for _ in range(M)]
lad = [[0 for n in range(N)] for h in range(H)]
for kka in range(M):
    y,x = lad_in[kka]
    lad[y-1][x-1] = 1
#for kka in range(H):
#    print(lad[kka])
res = 4

def checker():
    global lad,H,N
    #for kka in range(H):
    #    print(lad[kka])
    for x in range(N-1):
        i = x
        for y in range(H):
            #print(y,i,x)
            if lad[y][i] == 1:
                i += 1
            elif i != 0 and lad[y][i-1] == 1:
                i -= 1

        if i != x:
            return False
    return True

def dfs(y,x,cnt):
    global res,N,H,lad
    if cnt >= res:
        return
    if checker():
        res = min(cnt,res)
        return
    if cnt == 3:
        return
    for ny in range(y, H):
        for nx in range(x,N-1):
            if lad[ny][nx] == 0 and lad[ny][nx+1] == 0:
                lad[ny][nx] = 1
                dfs(ny,nx+2,cnt+1)
                lad[ny][nx] = 0

dfs(0,0,0)
print(res if res <= 3 else -1)
