import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # row col
arr = [list(map(int, input().split())) for _ in range(n)]
arr_max = 0  # 배열 원소 최대값   max(max(*arr))
for i in range(n):
    for j in range(m):
        arr_max = max(arr_max, arr[i][j])

# 방향 이동
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# 방문 체크
check = [[0] * m for _ in range(n)]

# 최종 답
ans = 0


def dfs(r, c, sum, cnt):
    global ans

    # 현재 sum에서 나머지가 모두 최대값일때, 기존 답을 못넘기면 dfs 종료
    if sum + (arr_max * (4 - cnt)) <= ans:
        return

    # 4개 연결 시 종료
    if cnt == 4:
        ans = max(ans, sum)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 범위 체크
        if nr >= 0 and nr < n and nc >= 0 and nc < m and not check[nr][nc]:
            if cnt == 2:    # ㅜ 케이스
                check[nr][nc] = 1   # 방문 체크
                dfs(r, c, sum + arr[nr][nc], cnt + 1)
                check[nr][nc] = 0   # 방문 해제

            check[nr][nc] = 1   # 방문 체크
            dfs(nr, nc, sum + arr[nr][nc], cnt + 1)
            check[nr][nc] = 0   # 방문 해제


# 모든 좌표에 대해 dfs
for i in range(n):
    for j in range(m):
        check[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        check[i][j] = 0

print(ans)
