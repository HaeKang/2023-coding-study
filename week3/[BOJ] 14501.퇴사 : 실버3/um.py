import sys

d_in = sys.stdin.readline
N = int(d_in())
dat = [list(map(int, d_in().split())) for kka in range(N)]
pt = [dat[kka][1] for kka in range(N)]
max_e_ic = 0
sums = [sum(pt[kka:]) for kka in range(N)]
#print(sums)
#print(len(sums))
def e_ic():
    #global dat
    global N
    val = 0
    dfs(val,0)

def dfs(val,n):
    global dat
    global max_e_ic
    if n < N:
        if val + sums[n] > max_e_ic:
            #print(dat[n][0], '   ', dat[n][1], "   ", n)
            if dat[n][0] <= N-n:
                # n 일차 상담 진행
                dfs(val+dat[n][1],n+dat[n][0])
            if dat[n][0] > 1:
                # n 일차 상담 진행 x
                dfs(val,n+1)

    max_e_ic = max(val,max_e_ic)

e_ic()
print(max_e_ic)