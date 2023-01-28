n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 0
max_val = max(map(max, arr))

def dfs(x, y, cnt, total):
    global ans
    if ans >= total + max_val * (4 - cnt):  #최대값이 안되면 종료
        return

    if cnt == 4: 
        ans = max(ans, total)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 2:   #ㅓ, ㅏ, ㅗ, ㅜ 의 경우
                visited[nx][ny] = True
                dfs(x, y, cnt + 1, total + arr[nx][ny]) # 직전 지점 x,y에서 dfs
                visited[nx][ny] = False
            visited[nx][ny] = True   #일반적인 경우 dfs
            dfs(nx, ny, cnt + 1, total + arr[nx][ny])
            visited[nx][ny] = False

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False

print(ans)