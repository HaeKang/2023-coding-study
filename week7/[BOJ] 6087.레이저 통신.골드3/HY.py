#메모리 초과
from collections import deque

w, h = map(int, input().split())
graph = []
for _ in range(h):
    graph.append(list(input()))

c = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            c.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[1e9] * w for _ in range(h)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if nx < 0 or nx >= h or ny < 0 or ny >= w:  #범위 벗어나는 경우
                    break
                if graph[nx][ny] == "*":   # 벽인 경우  
                    break
                if visited[nx][ny] < visited[x][y] + 1:  #최소가 아닌 경우
                    break
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                nx += dx[i]
                ny += dy[i]
                
start_x, start_y = c[0][0], c[0][1]
end_x, end_y = c[1][0], c[1][1]

bfs(start_x, start_y)

print(visited[end_x][end_y] - 1)