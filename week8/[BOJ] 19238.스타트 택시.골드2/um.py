import sys
from collections import deque
'''
승객 착을 때 거리가 같은 리스트 (리스트는 (y,x) 로 소트 된 것 처럼 만들거임)
에서 거리를 하나씩 늘리며 찾을거임 (북서동남 순)
승객 잇으면 종료

목적지도 거리 하나씩 늘려가며 같은 함수로 찾도록 하겟음

'''

in_d = sys.stdin.readline
N, M, F = list(map(int, in_d().split()))
mat = [list(map(int, in_d().split())) for _ in range(N)]
y, x = list(map(int, in_d().split()))
ps = [list(map(int, in_d().split())) for _ in range(M)]
dy = [-1,0,0,1] # 북 서 동 남
dx = [0,-1,1,0]

def find_road(sy,sx,des = False):
    global mat, F, N, ps
    Mt = len(ps)
    hmat = [[99999] * (N+1) for _ in range(N+1)]

    hmat[sy][sx] = 0
    '''
    if des == False:  # 현위치에서 승객있는 경우
        for kka in range(Mt):
            y, x, ey, ex = ps[kka]
            if y == sy and x == sx:
                return kka, 0
    else: # 현위치가 목적지인 경우
        (ny, nx) = des
        if ny == sy and nx == sx:
            return (ny,nx), 0
    '''

    Q = deque([(sy,sx,0)])
    while Q:
        (y,x,do) = Q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (not (0 < ny <= N and 0 < nx <= N)) or mat[ny-1][nx-1] == 1:
                continue
            nd = min(do + 1, hmat[ny][nx])
            if nd == do + 1:
                Q.append((ny, nx, nd))
            hmat[ny][nx] = nd
            ''' 최단 거리 승객 찾기를 최단 거리 찾기중 할 경우 시간초과
            따라서 맵에 최단거리 다 구하고 승객찾기
            if des == False: # 승객 찾는 경우
                for kka in range(Mt):
                    sy, sx, ey, ex = ps[kka]
                    if sy == ny and sx == nx:
                        #print('------------------------------------------',F,nd)
                        #for kki in range(N+1):
                        #    print(hmat[kki])
                        return kka, nd
            else:
                ey, ex = des
                if ny == ey and nx == ex:
                    #print('fdfdfdfdfd--------------',F,nd)
                    #for kka in range(N+1):
                    #    print(hmat[kka])
                    return (ny,nx), nd
            '''
    return hmat

fail_trig = False
for m in range(M):
    # 승객찾기
    hmat = find_road(y,x)
    if d > F or d < 0:
        fail_trig = True
        break
    F -= d
    y, x, ey, ex = ps[idx]
    del ps[idx]
    # 최단거리 찾기
    point, d = find_road(y,x,(ey,ex))
    if d > F or d < 0:
        fail_trig = True
        break
    (y,x) = point
    F += d
if not fail_trig:
    print(F)
else:
    print(-1)
