from collections import deque
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited= [[False]*m for _ in range(n)]
answer = 0
def dfs(x, y, cnt , total):
    global answer
    if cnt == 4:
        answer = max(answer, total)
        return
    for d in range(4):
        nx, ny = x+dx[d], y+dy[d]
        if not (0<= nx < n and 0<= ny < m) or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, cnt+1, total+arr[nx][ny])
        visited[nx][ny] = False

for x in range(n):
    for y in range(m):
        visited[x][y] = True
        dfs(x, y, 1, arr[x][y])
        visited[x][y] = False
        if y <= m-3 and x <= n-2:
            answer = max(answer, sum(arr[x][y:y+3])+arr[x+1][y+1])
        if 1<= y <= m-2 and x <= n-2:
            answer = max(answer, sum(arr[x+1][y-1:y+2]) + arr[x][y])
        if y<= m-2 and x <= n-3:
            answer = max(answer, arr[x][y]+arr[x+1][y]+arr[x+2][y]+arr[x+1][y+1])
        if 1<= x< n-2 and y <= m-2:
            answer = max(answer, arr[x][y]+arr[x-1][y+1]+arr[x][y+1]+arr[x+1][y+1])

print(answer)
