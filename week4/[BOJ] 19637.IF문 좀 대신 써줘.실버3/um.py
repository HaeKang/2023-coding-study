import sys

in_d = sys.stdin.readline
N,M = list(map(int,in_d().split()))
ching = [list(in_d().split()) for _ in range(N)]

def bs(num):
    st = 0
    en = N - 1
    re = 0
    while(st <= en):
        md = int((st+en)/2)
        if num > int(ching[md][1]):
            st = md + 1
        else:
            en = md - 1
            re = md

    return ching[re][0]

for m in range(M):
    print(bs(int(in_d())))


