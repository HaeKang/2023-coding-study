import sys
N, M = map(int, input().split())

name = []
val = []

for i in range(N):
    n, v = sys.stdin.readline().rstrip().split()
    name.append(n)
    val.append(int(v))

def get_name(v): # 이분탐색
    lo = 0
    hi = N-1
    while(lo < hi-1):
        mid = (lo + hi) // 2
        if v <= val[mid]:
            hi = mid
        elif v > val[mid]:
            lo = mid
    #print(lo, hi)

    if v > val[lo]:
        return hi
    else:
        return lo


ret = []
for j in range(M):
    ret.append(name[get_name(int(sys.stdin.readline().rstrip()))]) # O(MlogN)
for r in ret:
    print(r)