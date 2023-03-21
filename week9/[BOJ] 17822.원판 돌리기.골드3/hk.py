import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().split())  # n = row, m = col
arr = [list(map(int, input().split())) for _ in range(n)]

for _ in range(t):

    # 전체가 다 0으로 이루어져있으면 멈춤
    tmp_sum = 0
    for i in range(n):
        tmp_sum += sum(arr[i])

    if tmp_sum == 0:
        break

    # d : 0 시계, 1 : 반시계
    x, d, k = map(int, input().split())

    # 1번
    for x2 in range(x-1, n, x):
        if d == 0:
            tmp = deque(arr[x2])
            tmp.rotate(k)
            arr[x2] = list(tmp)
        else:
            tmp = deque(arr[x2])
            tmp.rotate(-k)
            arr[x2] = list(tmp)

    delete_list = []

    # 2번 - 같은 원반
    for i in range(n):
        for j in range(m-1):
            if arr[i][j] != 0:

                if j == 0:
                    if arr[i][j] == arr[i][-1]:
                        delete_list.append([i, j])
                        delete_list.append([i, m-1])

                if arr[i][j] != 0 and arr[i][j] == arr[i][j+1]:
                    delete_list.append([i, j])
                    delete_list.append([i, j+1])

    # 2번 - 다음 원반
    for j in range(m):
        for i in range(n-1):
            if arr[i][j] != 0:
                if arr[i][j] == arr[i+1][j]:
                    delete_list.append([i, j])
                    delete_list.append([i+1, j])

    # 2-2
    if len(delete_list) == 0:
        avg = 0
        zero = 0

        for i in range(n):
            avg += sum(arr[i])
            zero += arr[i].count(0)

        avg = avg / (n*m - zero)

        for i in range(n):
            for j in range(m):
                if arr[i][j] != 0:
                    if arr[i][j] > avg:
                        arr[i][j] -= 1
                    elif arr[i][j] < avg:
                        arr[i][j] += 1

    else:
        for x1, y1 in delete_list:
            arr[x1][y1] = 0

ans = 0
for i in range(n):
    ans += sum(arr[i])

print(ans)
