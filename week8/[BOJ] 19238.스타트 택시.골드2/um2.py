import sys
from collections import deque
'''
승객 착을 때 거리가 같은 리스트 (리스트는 (y,x) 로 소트 된 것 처럼 만들거임)
에서 거리를 하나씩 늘리며 찾을거임 (북서동남 순)
승객 잇으면 종료 -> 이렇게 승객 찾아버리면 시간 초과 (맵그릴때 겹치는부분도 잇었음)

목적지도 거리 하나씩 늘려가며 같은 함수로 찾도록 하겟음

최단 거리 맵 다 찾고 승객 찾아야함

'''

in_d = sys.stdin.readline
N, M, F = list(map(int, in_d().split()))
mat = [list(map(int, in_d().split())) for _ in range(N)]
y, x = list(map(int, in_d().split()))
ps = [list(map(int, in_d().split())) for _ in range(M)]
dy = [-1,0,0,1] # 북 서 동 남
dx = [0,-1,1,0]

def find_road(sy,sx):
    global mat, F, N, dy, dx
    hmat = [[-1] * (N+1) for _ in range(N+1)]
    hmat[sy][sx] = 0
    Q = deque([(sy,sx,0)])
    while Q: # 거리가 적을수록 리스트 왼족에 잇음
        (y,x,do) = Q.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if (not (0 < ny <= N and 0 < nx <= N)) or mat[ny-1][nx-1] == 1:
                continue
            if hmat[ny][nx] != -1: # 이부분이 없으면 겹치는 부분때문에 시간초과 됨 항상 최단거리를 찾을 수 밖에 없음
                continue
            nd = do + 1
            Q.append((ny, nx, nd))
            hmat[ny][nx] = nd

    return hmat

fail_trig = False
for m in range(M):
    # 승객찾기
    hmat = find_road(y,x)
    Mt = len(ps)
    nps = list()
    for kka in range(Mt):
        sy, sx, ey, ex = ps[kka]
        nps.append((hmat[sy][sx],sy,sx,kka))
    nps.sort()
    d, y, x, idx = nps[0]
    #for kka in range(N+1):
    #    print(hmat[kka])
    if d > F or d < 0: # 갈수 있는 거리인지 or 벽으로 막히지 않았는지 체크
        fail_trig = True
        break
    F -= d
    y, x, ey, ex = ps[idx]
    del ps[idx]

    # 최단거리 찾기
    hmat = find_road(y,x)
    #print(ey,ex)
    d = hmat[ey][ex]
    y, x = ey , ex
    if d > F or d < 0:
        fail_trig = True
        break
    F += d
if not fail_trig:
    print(F)
else:
    print(-1)
