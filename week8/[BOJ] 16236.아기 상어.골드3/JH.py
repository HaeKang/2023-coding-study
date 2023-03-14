# 참고: https://resilient-923.tistory.com/357

from collections import deque

N = int(input())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

def print_arr(arr):
    for i in range(N):
        print(' '.join(list(map(str, arr[i]))))
    print()

y,x = -1,-1
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            y = i; x = j

size = 2
time = 0
cnt = 0 

dy = [0,0,-1,1]
dx = [-1,1,0,0]
def bfs(y,x):
    cand = []

    visited = [[0] * N for i in range(N)]

    queue = deque()
    queue.append((y,x))
    visited[y][x] = 1

    while queue:
        current_y, current_x = queue.popleft()

        for i in range(4):
            next_y, next_x = current_y + dy[i], current_x + dx[i]
            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N and visited[next_y][next_x] == 0:
                if area[next_y][next_x] <= size:
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = visited[current_y][current_x] + 1 # visited를 활용하여 거리 계산

                    if area[next_y][next_x] < size and area[next_y][next_x] != 0:
                        cand.append((visited[next_y][next_x]-1, next_y, next_x)) # 후보 물고기들을 리스트에 담기

    return sorted(cand, key=lambda x:(x[0], x[1], x[2])) # x[0], x[1], x[2] 순으로 정렬

while True:

    cand = bfs(y,x) # 현재 위치에서의 bfs

    if len(cand) < 1:
        break

    step, next_y, next_x = cand[0]
    time += step # step
    area[y][x] = area[next_y][next_x] = 0

    y,x = next_y,next_x

    cnt += 1
    if cnt == size: # 사이즈 업
        size += 1
        cnt = 0

print(time)