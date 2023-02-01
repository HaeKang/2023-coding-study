n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
    
visited = [[False] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True    #방문처리
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:  #범위 안에 있고
            if not visited[nx][ny] and graph[nx][ny] == 1: #1이면서 방문하지 않았으면 dfs
                dfs(nx, ny)
        
cnt = 0
result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i, j)
            result.append(cnt)
            cnt = 0
            
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])