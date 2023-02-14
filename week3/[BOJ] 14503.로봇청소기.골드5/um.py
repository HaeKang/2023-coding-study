import copy
import sys

in_d = sys.stdin.readline
N,M = list(map(int, in_d().split()))
r,c,hd_d = list(map(int, in_d().split()))
dat = [list(map(int, in_d().split())) for _ in range(N)]

clean_mat = copy.deepcopy(dat)
cln = 0
dx = [0,1,0,-1]
dy = [-1,0,1,0]

def run():
    global dat,r,c,hd_d,cln,clean_mat
    back_trig = False
    while(True):
        if clean_mat[r][c] == 0:
            cln += 1
            clean_mat[r][c] = 1
        trig = False
        for kka in range(4):
            hd_d -= 1
            hd_d = hd_d % 4
            #print(hd_d)
            ny = r + dy[hd_d]
            nx = c + dx[hd_d]
            if clean_mat[ny][nx] == 0:
                r = ny
                c = nx
                trig = True
                break
            else:
                continue
        if trig:
            back_trig = False
            continue

        ny = r + dy[hd_d - 2]
        nx = c + dx[hd_d - 2]
        if dat[ny][nx] == 1:
            break
        r = ny
        c = nx
        if back_trig:
            continue
            break
        back_trig = True


run()
print(cln)
