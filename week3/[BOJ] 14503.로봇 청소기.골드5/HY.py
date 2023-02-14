n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
    
def turn():
    global d
    d = (d - 1) % 4

ans = 1
visited[x][y] = 1
flag = 0   #turn 확인용

while True:
    turn()
    nx = x + dx[d]
    ny = y + dy[d]
    
    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
        visited[nx][ny] = 1
        ans += 1
        x = nx
        y = ny
        flag = 0
        continue
    else:
        flag += 1
        
    if flag == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == 0:
            x = nx
            y = ny
            flag = 0
        else:
            break
            
print(ans)