m, h, n = map(int, input().split())
#가로선 연속하는 경우 x > 새로운 가로선은 양옆이 비어있어야함

arr = [[0]*m for _ in range(n)]
for _ in range(h):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1

def check():
    global m, n, arr
    for y in range(m):
        nx, ny = 0, y
        visited = [[False] * (m) for _ in range(n)]
        while 0<= nx < n:
            if not visited[nx][ny] and arr[nx][ny] == 1:
                ny += 1
                visited[nx][ny] = True
            elif not visited[nx][ny] and arr[nx][ny] == -1:
                ny -= 1
                visited[nx][ny] = True
            else:
                nx += 1

        if ny != y:
            return False
    return True


answer = 4

def dfs(i, j, cnt):
    global answer, arr
    if cnt >= answer or cnt >= 4:
        return

    if check():
        answer = min(answer, cnt)
        return

    for x in range(max(i-1, 0), n):
        for y in range(max(j-1, 0), m-1):
            if arr[x][y] == 0 and arr[x][y+1] == 0:
                arr[x][y] = 1
                arr[x][y + 1] = -1
                dfs(x, y, cnt + 1)
                arr[x][y] = 0
                arr[x][y + 1] = 0
    return


if m == 1:
    print(0)
else:
    dfs(0, 0, 0)
    if answer >= 4:
        answer = -1
    print(answer)
