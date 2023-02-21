## pypy3 정답
## python3 시간 초과: dfs에서 더 줄일 부분이 있을지 궁금..

import sys 

N,M = map(int, sys.stdin.readline().rstrip().split())

paper = []
for i in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_sum = 0

dy = [-1,1,0,0]
dx = [0,0,-1,1]

visited = []
def dfs(current):
    global max_sum, visited
    if len(visited) == 4: # 4군데 다 돌았으면 값을 다 더해서 이전 max_sum과 비교
        candidate = 0
        for v in visited:
            candidate += paper[v[0]][v[1]]
        max_sum = max(candidate, max_sum)
        return

    y, x = current
    for i in range(4):
        next_y, next_x = y+dy[i], x+dx[i]

        if next_y >= N or next_x >= M or next_y < 0 or next_x < 0:
            continue

        if not (next_y,next_x) in visited:
            visited.append((next_y, next_x))
            dfs((next_y, next_x))
            visited.pop()


def manual(current):
    global max_sum
    y, x = current

    # ㅗ
    if y-1 >= 0 and x-1 >= 0 and x+1 < M:
        candidate = paper[y][x] + paper[y-1][x] + paper[y][x-1] + paper[y][x+1]
        max_sum = max(candidate, max_sum)
    # ㅜ
    if y+1 < N and x-1 >= 0 and x+1 < M:
        candidate = paper[y][x] + paper[y+1][x] + paper[y][x-1] + paper[y][x+1]
        max_sum = max(candidate, max_sum)

    # ㅓ
    if y + 1 < N and y - 1 >= 0 and x - 1 >= 0:
        candidate = paper[y][x] + paper[y+1][x] + paper[y-1][x] + paper[y][x-1]
        max_sum = max(candidate, max_sum)

    # ㅏ
    if y + 1 < N and y - 1 >= 0 and x + 1 < M:
        candidate = paper[y][x] + paper[y+1][x] + paper[y-1][x] + paper[y][x+1]
        max_sum = max(candidate, max_sum)


for i in range(N):
    for j in range(M):
        visited.append((i,j)) # 모든 위치에서 dfs 다 돌려보기
        dfs((i,j))
        visited.pop()
        manual((i,j))

print(max_sum)