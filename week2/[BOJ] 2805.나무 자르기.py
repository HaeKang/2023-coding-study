import sys

N,M = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))
tree.sort()

lo = 0
hi = tree[-1]

while(lo <= hi): # 이분 탐색: 더 높은 높이로 자르는 경우는 고려 안해도 됨. 경계값을 찾는 문제라서?

    mid = (lo + hi) // 2

    ret = 0
    for t in tree:
        if t > mid:
            ret += t-mid

    if ret >= M:
        lo = mid+1
    else:
        hi = mid-1

print(hi)