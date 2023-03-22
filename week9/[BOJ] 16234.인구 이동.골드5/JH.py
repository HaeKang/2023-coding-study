from collections import deque

N,L,R = map(int, input().split())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

def test_print(arr):
    for i in range(N):
        print(' '.join(list(map(str, arr[i]))))
    print()

dy = [-1,1,0,0]
dx = [0,0,-1,1]

visited = [[0] * N for i in range(N)]
team = 1

def bfs(y,x):
    global visited, area

    q = deque()
    q.append((y,x))
    visited[y][x] = team

    apply_q = deque()

    while q:
        i,j = q.popleft()
        apply_q.append((i,j)) # 연합 인구 계산할 queue

        for d in range(4):
            next_y, next_x = i + dy[d], j + dx[d]
            if 0 <= next_y < N and 0 <= next_x < N and visited[next_y][next_x] == 0 and L <= abs(area[i][j] - area[next_y][next_x]) <= R: # 연합이 가능하면
                visited[next_y][next_x] = team # visited에 연합 표시
                q.append((next_y,next_x)) # 다음 queue로

    population = 0
    for y,x in apply_q:
        population += area[y][x]
    population //= len(apply_q) # 연합 인구 계산

    while apply_q:
        y,x = apply_q.popleft()
        area[y][x] = population # 연합 인구 적용

time = 0
while True:
    team = 1 
    visited = [[0] * N for i in range(N)]

    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                bfs(y,x)
                team += 1 # 연합을 표시한다

    if visited[-1][-1] == N*N: # 종료 조건: 모든 국가가 개별 연합일 때
        break

    time += 1

print(time)