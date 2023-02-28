import sys

in_d = sys.stdin.readline
N = int(in_d())
dc = [list(map(int, in_d().split())) for _ in range(N)] # xydg

dy = [0,-1,0,1]
dx = [1,0,-1,0]

mat = [[False]*101 for _ in range(101)]
minx,miny,maxx,maxy = 0,0,100,100

def gc(x,y,d,g):
    global mat, dy, dx, minx, miny, maxx, maxy
    rp_y, rp_x = y + dy[d], x + dx[d]
    gc_p_y, gc_p_x = [y,rp_y], [x,rp_x]
    for gen in range(g):
        t_getsu = len(gc_p_y)
        for i in range(t_getsu):
            n_gc_p_y = gc_p_x[i] - rp_x + rp_y
            n_gc_p_x = -(gc_p_y[i] - rp_y) + rp_x
            gc_p_y.append(n_gc_p_y)
            gc_p_x.append(n_gc_p_x)
        rp_y = gc_p_y[t_getsu]
        rp_x = gc_p_x[t_getsu]

    for i in range(len(gc_p_y)):
        mat[gc_p_y[i]][gc_p_x[i]] = True
    minxp = min(gc_p_x)
    minx = min(minxp,minx)
    minyp = min(gc_p_y)
    miny = min(minyp,miny)

    maxxp = max(gc_p_x)
    maxx = max(maxx,maxxp)
    maxyp = max(gc_p_y)
    maxy = max(maxy,maxyp)
    return

def counter():
    global mat, minx, miny, maxx, maxy
    cnt = 0
    for y in range(miny,maxy):
        for x in range(minx,maxy):
            if mat[y][x] and mat[y+1][x] and mat[y][x+1] and mat[y+1][x+1]:
                cnt += 1
    print(cnt)

for x,y,d,g in dc:
    gc(x,y,d,g)
counter()
