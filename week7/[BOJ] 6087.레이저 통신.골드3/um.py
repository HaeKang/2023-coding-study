import sys

in_d = sys.stdin.readline
W, H = list(map(int, in_d().split()))

mat = [list(in_d().split('\n')[0]) for _ in range(H)]
st_y, st_x, en_y, en_x = False, False, False, False
Cs = list()
for y in range(H):
    for x in range(W):
        if mat[y][x] == 'C':
            Cs.append((y,x))
(st_y, st_x), (en_y, en_x) = Cs #False, False, False, False
dx = [1,0,-1,0]
dy = [0,1,0,-1]
res = [100000]

def find(y, x, dir, c):
    global res, mat, dy, dx, st_y, st_x, en_y, en_x
    if min(res) <= c:
        return
    #print('---------------')
    #for h in range(H):
    #    print(mat[h])
    mins_y, mins_x = list(), list()
    for kka in range(100):
        ny, nx = y + dy[dir] * (kka + 1), x + dx[dir] * (kka + 1)
        if (not (0 <= nx < W and 0 <= ny < H)) or mat[ny][nx] == '*':
            break
        if (ny,nx) == (en_y,en_x):
            res.append(c)
            return
            #break
        if mat[ny][nx] != 'C':
            if mat[ny][nx] == '.' or mat[ny][nx] > c:
                mat[ny][nx] = c
                mins_y.append(ny)
                mins_x.append(nx)
    dirr = 5
    for rr in range(2):
        if rr == 0:
            dirr = (dir - 1) % 4
        else:
            dirr = (dir + 1) % 4
        for kki in range(len(mins_x)):
            find(mins_y[-kki-1],mins_x[-kki-1], dirr, c + 1)


for kka in range(4):
    find(st_y, st_x, kka, 0)

#print(res)
print(min(res))