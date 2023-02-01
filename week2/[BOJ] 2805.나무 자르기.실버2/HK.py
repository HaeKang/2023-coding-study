"""
https://www.acmicpc.net/problem/2805

"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 나무 자르기 (return : 집에 가져가는 나무 길이)


def cut_tree(cut_size):
    global m
    tree = 0
    for data in arr:
        if data > mid:
            tree += data - cut_size
            if tree >= m:   # m미터만 넘으면 종료 (시간초과 방지)
                return True

    return False


start = 0
end = max(arr)
ans = 0

# 이분탐색
while start <= end:
    mid = (start + end) // 2
    if cut_tree(mid):
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1
print(ans)
