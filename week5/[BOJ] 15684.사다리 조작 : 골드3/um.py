import sys
from collections import Counter
# gggggggggggggg

in_d = sys.stdin.readline
N,M,H = list(map(int,in_d().split()))
lad_in = [list(map(int,in_d().split())) for _ in range(M)]
lad = [[0 for n in range(N)] for h in range(H)]
for kka in range(M):
    y,x = lad_in[kka]
    lad[y-1][x-1] = 1
    lad[y-1][x] = -1
#for kka in range(H):
#    print(lad[kka])
cnt = 0
res = 4

def checker(i):
    global lad,H
    p,m,io = 0, 0, i
    for y in range(H):
        if lad[y][i] == 1:
            i += 1
        elif lad[y][i] == -1:
            i -= 1
        if lad[y][io] == 1:
            p += 1
        elif lad[y][io] == -1:
            m += 1
    p %= 2
    m %= 2
    return [i,p,m]

def lad_put(y,i,rl):
    global lad, cnt, N
    if rl == 1:
        if (not 0 <= i+rl < N) or lad[y][i+rl] != 0:
            #print('rout')
            return False
        else:
            lad[y][i] = 1
            lad[y][i+rl] = -1
    elif rl == -1:
        if not 0 <= i+rl < N or lad[y][i+rl] != 0:
            #print('lout')
            return False
        else:
            lad[y][i] = -1
            lad[y][i + rl] = 1
    cnt += 1
    print('lad put' ,y,i)
    return True

def lad_pop(y, i, rl):
    global lad, cnt
    lad[y][i] = 0
    lad[y][i + rl] = 0
    cnt -= 1

def dfs(tu):
    global H,res,cnt
    trig = -1
    for kka in range(N-1):
        if checker(kka)[0] != kka:
            trig = kka
            break
    if trig == -1:
        res = min(cnt,res)
        return True

    if cnt >= 3:
        return False

    for kka in range(N-1,trig-1,-1):
        i,p,m = checker(kka)
        print('    '*tu,'kka' ,kka,i,p,m)
        if p != 0 or m != 0:
            #print(p,m)
            rl = -1
            if p != 0:
                rl = 1
            elif m != 0:
                rl = -1

            for ny in range(H):
                if lad[ny][kka] == 0:
                    #print('---',ny,kka)
                    if lad_put(ny,kka,rl):
                        dfs(tu+1)
                        lad_pop(ny,kka,rl)
        print('    '*tu,'kka' ,kka,i,p,m, '     end')


dfs(0)
#print('resussss')
if res > 3:
    print(-1)
else:
    print(res)