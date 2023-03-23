N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(a, b):
    tmp = []
    tmp.append((a, b))

    que = []
    que.append((a, b))
    while que:
        x, y = que.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0 and L <= abs(A[nx][ny] - A[x][y]) <= R:
                visited[nx][ny] = 1
                que.append((nx, ny))
                tmp.append((nx, ny))
    return tmp


anw = 0
while True:
    visited = [[0] * (N + 1) for _ in range(N + 1)]
    welcome = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1

                country = bfs(i, j)

                if len(country) > 1:
                    welcome = 1
                    num = sum([A[a][b] for a, b in country]) // len(country)
                    for a, b in country:
                        A[a][b] = num
    if welcome == 0:
        break

    anw += 1


print(anw)
