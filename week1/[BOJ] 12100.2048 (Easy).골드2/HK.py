import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split(" "))) for _ in range(n)]

dr = [1, -1, 0, 0]  # 아래 위
dc = [0, 0, -1, 1]  # 왼 오

# 왼쪽


def move_left(tmp_arr):
    for r in range(n):
        prev_col = 0    # 합쳐지지않은 값이 있는 마지막 col
        for c in range(1, n):
            if tmp_arr[r][c] != 0:
                tmp = tmp_arr[r][c]
                tmp_arr[r][c] = 0

                if tmp_arr[r][prev_col] == 0:
                    tmp_arr[r][prev_col] = tmp  # 옮기기

                elif tmp_arr[r][prev_col] == tmp:
                    tmp_arr[r][prev_col] *= 2   # 합치기
                    prev_col += 1

                else:   # 다른값인 케이스
                    prev_col += 1
                    tmp_arr[r][prev_col] = tmp  # 바로 옆으로 붙이기

    return tmp_arr

# 오른쪽


def move_right(tmp_arr):
    for r in range(n):
        prev_col = n-1
        for c in range(n-2, -1, -1):
            if tmp_arr[r][c] != 0:
                tmp = tmp_arr[r][c]
                tmp_arr[r][c] = 0

                if tmp_arr[r][prev_col] == 0:
                    tmp_arr[r][prev_col] = tmp

                elif tmp_arr[r][prev_col] == tmp:
                    tmp_arr[r][prev_col] *= 2   # 합치기
                    prev_col -= 1

                else:
                    prev_col -= 1
                    tmp_arr[r][prev_col] = tmp

    return tmp_arr

# 위


def move_up(tmp_arr):
    for c in range(n):
        prev_row = 0
        for r in range(1, n):
            if tmp_arr[r][c] != 0:
                tmp = tmp_arr[r][c]
                tmp_arr[r][c] = 0

                if tmp_arr[prev_row][c] == 0:
                    tmp_arr[prev_row][c] = tmp

                elif tmp_arr[prev_row][c] == tmp:
                    tmp_arr[prev_row][c] *= 2
                    prev_row += 1

                else:
                    prev_row += 1
                    tmp_arr[prev_row][c] = tmp

    return tmp_arr

# 아래


def move_down(tmp_arr):
    for c in range(n):
        prev_row = n-1
        for r in range(n-2, -1, -1):
            if tmp_arr[r][c] != 0:
                tmp = tmp_arr[r][c]
                tmp_arr[r][c] = 0

                if tmp_arr[prev_row][c] == 0:
                    tmp_arr[prev_row][c] = tmp

                elif tmp_arr[prev_row][c] == tmp:
                    tmp_arr[prev_row][c] *= 2
                    prev_row -= 1

                else:
                    prev_row -= 1
                    tmp_arr[prev_row][c] = tmp

    return tmp_arr


def get_max(tmp_arr):
    max_val = 0
    for r in range(len(tmp_arr)):
        for c in range(len(tmp_arr[0])):
            if tmp_arr[r][c] > max_val:
                max_val = tmp_arr[r][c]
    return max_val


def bfs():
    ans = 0  # 최종 답

    q = deque()
    cnt = 0
    q.append((arr, cnt))

    while q:
        n_arr, n_cnt = q.popleft()

        # 5번 움직였으면 stop
        if n_cnt == 5:
            if get_max(n_arr) > ans:
                ans = get_max(n_arr)
            continue

        # 아래 위 왼 오
        for i in range(4):
            copy_arr = copy.deepcopy(n_arr)
            if i == 0:
                q.append((move_down(copy_arr), n_cnt + 1))
            elif i == 1:
                q.append((move_up(copy_arr), n_cnt + 1))
            elif i == 2:
                q.append((move_left(copy_arr), n_cnt + 1))
            else:
                q.append((move_right(copy_arr), n_cnt + 1))

    return ans


print(bfs())
