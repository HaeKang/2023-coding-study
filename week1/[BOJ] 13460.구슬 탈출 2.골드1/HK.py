from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # r, c
arr = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

r_row, r_col = 0, 0   # 빨간공
b_row, b_col = 0, 0   # 파란공

for i in range(n):
    arr.append(list(input()))
    for j in range(m):
        if arr[i][j] == 'R':
            r_row = i
            r_col = j

        if arr[i][j] == 'B':
            b_row = i
            b_col = j


def move(r, c, dr, dc):
    move_cnt = 0  # 구슬이 이동한 횟수
    while arr[r + dr][c + dc] != '#' and arr[r][c] != 'O':
        r += dr
        c += dc
        move_cnt += 1

    return r, c, move_cnt


def bfs():
    cnt = 0
    check = []  # 방문여부

    q = deque()
    q.append((r_row, r_col, b_row, b_col, cnt))
    check.append([r_row, r_col, b_row, b_col])

    while q:
        nr_row, nr_col, nb_row, nb_col, n_cnt = q.popleft()

        # cnt는 10 이하
        if n_cnt >= 10:
            return -1

        for i in range(4):
            next_r_row, next_r_col, r_move_cnt = move(
                nr_row, nr_col, dr[i], dc[i])
            next_b_row, next_b_col, b_move_cnt = move(
                nb_row, nb_col, dr[i], dc[i])

            # 파란 구슬 통과 -> 실패
            if arr[next_b_row][next_b_col] == 'O':
                continue

            # 빨간 구슬만 통과
            if arr[next_r_row][next_r_col] == 'O':
                return n_cnt + 1

            # 빨간구슬, 파란구슬 같은 위치 안되도록 세팅 -> 많이 움직인애 뒤로
            if next_r_row == next_b_row and next_r_col == next_b_col:
                if r_move_cnt > b_move_cnt:
                    next_r_row -= dr[i]
                    next_r_col -= dc[i]
                else:
                    next_b_row -= dr[i]
                    next_b_col -= dc[i]

            if [next_r_row, next_r_col, next_b_row, next_b_col] not in check:
                check.append([next_r_row, next_r_col, next_b_row, next_b_col])
                q.append((next_r_row, next_r_col,
                          next_b_row, next_b_col, n_cnt + 1))

    return -1


print(bfs())
