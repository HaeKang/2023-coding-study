dy = [0, -1, 0, 1]#왼아래오 위
dx = [1, 0, -1, 0]
n = int(input())
arr = [[False]*102 for _ in range(102)]
def make_dirs(d, g):
    dirs = [d]
    for _ in range(g):
        new = [(d+1)%4 for d in dirs[::-1]]
        dirs.extend(new)
    return dirs


answer = 0
for _ in range(n):
    x, y, d, g = map(int, input().split())
    dirs = make_dirs(d, g)
    arr[x][y] = True
    for d in dirs:
        x, y = x+dx[d], y+dy[d]
        arr[x][y] = True

dx = [0, 1, 0, 1]#아래오 eorkr
dy = [0, 0, 1, 1]
for x in range(101):
    for y in range(101):
        check = True
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if not arr[nx][ny]:
                check = False
                break
        if check:
            answer += 1

print(answer)
