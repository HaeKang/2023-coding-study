import sys
input = sys.stdin.readline

# 0세대 : 0
# 1세대 : 0 1
# 2세대 : 0 1 2 1
# 3세대 : 0 1 2 1 2 3 2 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())

arr_max = 101
arr = [[0] * arr_max for _ in range(arr_max)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    arr[x][y] = 1

    # 0세대
    if g == 0:
        nx = x + dx[d]
        ny = y + dy[d]
        arr[nx][ny] = 1

    # n세대
    else:
        move_lst = [d]

        for _ in range(g):
            move = []
            for i in range(len(move_lst) - 1, -1, -1):
                tmp_move = move_lst[i] + 1
                if tmp_move == 4:
                    tmp_move = 0
                move.append(tmp_move)
            move_lst.extend(move)

        for m in move_lst:
            nx = x + dx[m]
            ny = y + dy[m]
            arr[nx][ny] = 1
            x = nx
            y = ny

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            ans += 1

print(ans)
