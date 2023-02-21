import sys

in_d = sys.stdin.readline
N = int(in_d())
mat = [list(map(int, in_d().split())) for _ in range(N)]
''' dfs 시간 초과
cnt = 0
def dfs(y,x):
    global mat,N,cnt
    val = mat[y][x]
    if val < 0:
        return val
    th_p = 0

    if y == N-1 and x == N-1:
        cnt += 1
        return 0

    if y+val < N:
        th_p_y = dfs(y+val,x)
        if th_p_y == 0:
            th_p -= 1
        else:
            th_p += th_p_y
    if x+val < N:
        th_p_x = dfs(y,x+val)
        if th_p_x == 0:
            th_p -= 1
        else:
            th_p += th_p_x

    mat[y][x] = th_p
    return th_p

dfs(0,0)
'''
''' 
# DP 출구부터 시작 / 출구까지 갈수있는 경우의 수 더하기 / 틀림. 반례 못찾겠음.
res = [[0 for x in range(N)] for y in range(N)]
for kka in range(N-2,-1,-1):
    # y
    ny = kka + mat[kka][3]
    if ny < N and (mat[ny][3] == 0 or res[ny][3] > 0):
        res[kka][3] = 1
    # x
    nx = kka + mat[3][kka]
    if nx < N and (mat[3][nx] == 0 or res[3][nx] > 0):
        res[3][kka] = 1

for y in range(N-2,-1,-1):
    for x in range(N-2,-1,-1):
        ny = y + mat[y][x]
        nx = x + mat[y][x]
        if ny < N and res[ny][x] > 0:
            res[y][x] += res[ny][x]
        if nx < N and res[y][nx] > 0:
            res[y][x] += res[y][nx]

print(res[0][0])
'''

# DP 입구 부터 찾기

res = [[0 for x in range(N)] for y in range(N)]
res[0][0] = 1
for y in range(N):
    for x in range(N):
        if y == N - 1 and x == N - 1:
            break
        ny = y + mat[y][x]
        nx = x + mat[y][x]
        if ny < N:
            res[ny][x] += res[y][x]
        if nx < N:
            res[y][nx] += res[y][x]

        #print(y,x,'================')
        #for kka in range(N):
        #    print(res[kka])
print(res[N-1][N-1])
