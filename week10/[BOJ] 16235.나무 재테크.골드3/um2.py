import sys
from collections import deque
import time
# python3 시간초과 pypy3 936 ms

in_d = sys.stdin.readline
N, M, K = list(map(int, in_d().split()))
mat_i = [list(map(int, in_d().split())) for _ in range(N)]
mat = [[[5, mat_i[y][x], 0, 0] for x in range(N)] for y in range(N)] # NxN 에 [현재양분, 겨울에추가되는양분(input), 최근업데이트년도, 추가할양분]
namus = [[deque() for x in range(N)] for y in range(N)]
for _ in range(M):
    y,x,k = list(map(int, in_d().split()))
    namus[y-1][x-1].append(k)
dy = [0,1,1,1,0,-1,-1,-1]
dx = [1,1,0,-1,-1,-1,0,1]

t1 = time.time()
for kka in range(10000):
    for t in range(K):
        # winter, spring, summer
        for y in range(N):
            for x in range(N):
                getsu = len(namus[y][x])
                for _ in range(getsu):
                    k = namus[y][x].popleft()
                    if mat[y][x][2] != t: # 최근 업데이트 년도가 현재 년도가 아니면
                        mat[y][x][0] += mat[y][x][3] # 작년에 죽은애들 더해주고 (여름)
                        mat[y][x][3] = 0 # 작년에 죽은 애들 초기화
                        mat[y][x][0] += (t - mat[y][x][2]) * mat[y][x][1] # 업데이트 빼먹은만큼 양분넣어주고 (겨울)
                        mat[y][x][2] = t # 업데이트한 년도 현재 년도로 바꿈

                    if mat[y][x][0] >= k:
                        mat[y][x][0] -= k
                        namus[y][x].append(k+1) # 나이 많을테니 오른쪽에 넣어주고
                    else:
                        mat[y][x][3] += int(k/2) # 죽은 애들 다음 양분 업데이트할때 더해줄 값
        # fall
        for y in range(N):
            for x in range(N):
                for k in namus[y][x]:
                    if k % 5 == 0:
                        for d in range(8):
                            ny, nx = y + dy[d], x + dx[d]
                            if not (0 <= nx < N and 0 <= ny < N):
                                continue
                            namus[ny][nx].appendleft(1) # 번식은 왼쪽에 제일 나이어린 나무 추가
print('ttt', time.time()-t1)

getsu = 0
for y in range(N):
    for x in range(N):
        getsu += len(namus[y][x])
print(getsu)
