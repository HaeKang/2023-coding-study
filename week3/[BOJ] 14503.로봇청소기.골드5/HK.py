import sys
input = sys.stdin.readline

n, m = map(int, input().split())
robot_r, robot_c, robot_dir = map(int, input().split())

# 북 0 동 1 남 2 서 3
# 0 -> 3 -> 2 -> 1 순으로 가야함
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 1

# 청소 시 2으로 변경


def dfs(r, c, dir):
    global cnt

    # 1번
    arr[r][c] = 2   # 청소 완료
    check = 0

    for _ in range(4):
        # 2번 -> 왼쪽방향 탐색 (0->3->2->1)
        if dir == 0:
            dir = 3
        else:
            dir -= 1

        nr = r + dr[dir]
        nc = c + dc[dir]

        # 범위체크, 빈칸체크
        if (nr >= 0 and nr < n and nc >= 0 and nc < m) and arr[nr][nc] == 0:
            cnt += 1    # 청소 개수 ++
            dfs(nr, nc, dir)    # 2-1
            check = 1
            break

    # 3번, 4번 (네 방향 모두 청소 못한케이스)
    if check == 0:
        # 4번 (후진 시 벽)
        if arr[r - dr[dir]][c - dc[dir]] == 1:
            return
        else:
            dfs(r-dr[dir], c-dc[dir], dir)  # 3번


dfs(robot_r, robot_c, robot_dir)
print(cnt)
