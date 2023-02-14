import sys

in_d = sys.stdin.readline
N,M = list(map(int, in_d().split()))
dat = [list(map(int, in_d().split())) for _ in range(N)]
od = int(in_d())
od_list = [list(map(int, in_d().split())) for _ in range(od)]

nm = [[0 for x in range(M + 1)] for y in range(N + 1)]
for dy in range(N):
    for dx in range(M):
        nm[dy + 1][dx + 1] = nm[dy + 1][dx] + nm[dy][dx + 1] + dat[dy][dx] - nm[dy][dx]

for kka in range(od):
    s = od_list[kka][:2]
    e = od_list[kka][2:]

    val = nm[e[0]][e[1]] - nm[e[0]][s[1]-1] - nm[s[0]-1][e[1]] + nm[s[0]-1][s[1]-1]

    print(val)
