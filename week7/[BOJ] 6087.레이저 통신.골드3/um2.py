import sys
from collections import deque

in_d = sys.stdin.readline
W, H = list(map(int, in_d().split()))
mat = list()
st_y, st_x, en_y, en_x = False,False, False, False
Cs = list()
for y in range(H):
    mat.append(list(in_d().split('\n')[0]))
    for x in range(W):
        if mat[y][x] == 'C':
            Cs.append((y,x))
(st_y,st_x),(en_y,en_x) = Cs
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs():
    global mat, dy, dx, st_y,st_x , W, H ,en_y,en_x
    check = [[10000000] * W for _ in range(H)]
    check[st_y][st_x] = -1
    Q = deque([(st_y,st_x)])

    while Q:
        print('----------------')
        for kka in range(H):
            print(check[kka])
        y,x = Q.popleft()
        print(y,x)
        if (y,x) == (en_y,en_x):
            return check[y][x]

        for i in range(4):
            ny,nx = y + dy[i], x + dx[i]
            while True:
                if (not (0 <= nx < W and 0 <= ny < H)) or mat[ny][nx] == '*':
                    break
                if check[ny][nx] < check[y][x] + 1:
                    break
                Q.append((ny,nx))
                check[ny][nx] = check[y][x] + 1
                ny,nx = y + dy[i], x + dx[i]


print(bfs())