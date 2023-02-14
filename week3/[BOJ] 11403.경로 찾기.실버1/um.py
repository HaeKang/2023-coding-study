import sys

in_d = sys.stdin.readline
N = int(in_d())
mat = [list(map(int, in_d().split())) for kka in range(N)]
out = [mat[kki][:] for kki in range(N)]

def dfs(st,de,chk): # st : start 지점 변하지않음, de : 목적지
    global N
    global out
    global mat
    out[st][de] = 1
    if chk[de]:
        return
    chk[de] = True
    for kka in range(len(mat[de])):
        dfs(st,mat[de][kka][1],chk)

def road(y,x):
    global mat
    global N
    for n in range(N):
        temp = list()
        for m in range(N):
            if mat[n][m] == 1:
                temp.append([n,m])
        mat[n] = temp # 입력의 경로가 있는 경우만 모아서 행이  N 개의 list 로 만듬
    for n in range(N):
        if len(mat[n]) == 0:
            continue
        chk = [False for _ in range(N)] # 방문체크
        chk[n] = True
        for kka in range(len(mat[n])):
            dfs(n,mat[n][kka][1],chk)

road(0,0)

for n in range(N):
    for m in range(N):
        if m != N-1:
            print(out[n][m],end=' ')
        else:
            print(out[n][m])#,end=' ')
