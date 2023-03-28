# pypy

import sys
N = int(input())

area = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

cnt = 0
def find_path(current_dir, current_end_pos):
    global cnt

    if current_end_pos == (N-1,N-1):
        cnt += 1
        return

    y, x = current_end_pos
    
    # 가로, 세로, 대각에 해당할 때
    if y + 1 < N and x + 1 < N:
        if area[y+1][x+1] == 0 and area[y+1][x] == 0 and area[y][x+1] == 0:
            find_path(2, (y+1,x+1))
    
    # 가로, 대각
    if current_dir == 0 or current_dir == 2:
        if x+1 < N and area[y][x+1] == 0:
            find_path(0, (y, x+1))

    if current_dir == 1 or current_dir == 2:
        if y+1 < N and area[y+1][x] == 0:
            find_path(1, (y+1, x))

start = (0,1)
d = 0
if area[N-1][N-1] == 0:
    find_path(d, start)
print(cnt)