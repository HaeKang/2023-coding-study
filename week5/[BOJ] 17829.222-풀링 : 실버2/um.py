import sys

in_d = sys.stdin.readline
N = int(in_d())
mat = [list(map(int,in_d().split())) for kka in range(N)]
No = N

def sec(m):
    m.sort()
    return m[-2]

def cal(n):
    global N,mat
    if pow(2,n) == No:
        #print('rree')
        return
    #print(n)
    N = int(N/2)
    for y in range(N):
        for x in range(N):
            dat = [mat[2*y][2*x], mat[2*y+1][2*x], mat[2*y][2*x+1], mat[2*y+1][2*x+1]]
            mat[y][x] = sec(dat)
    cal(n+1)

cal(0)
#print()
print(mat[0][0])