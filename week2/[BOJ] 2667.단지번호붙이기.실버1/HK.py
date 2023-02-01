n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
check = [[0] * n for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 0  # 단지 수
home_cnt = 0    # 집 개수 구하는 변수
homes = []   # 단지 별 집 개수


def dfs(r, c):
    global home_cnt
    home_cnt += 1   # 집 개수

    check[r][c] = 1

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue

        if check[nr][nc] == 1 or arr[nr][nc] == 0:
            continue

        dfs(nr, nc)


for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 and check[i][j] == 0:
            cnt += 1
            dfs(i, j)
            homes.append(home_cnt)
            home_cnt = 0

print(cnt)
homes = sorted(homes)
for data in homes:
    print(data)
