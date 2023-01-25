from collections import deque, defaultdict
n = int(input())
k = int(input())
arr = [[0]*n for _ in range(n)]
apples = []
for _ in range(k):
    x, y= map(int, input().split())
    arr[x-1][y-1] = 10

L = int(input())
dirs = defaultdict(lambda :'')
for _ in range(L):
    temp = list(input().split())
    x, c = int(temp[0]), temp[1]

    dirs[x] = c
# L이면 왼쪽으로 90, R이면 오른쪽으로
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# n, n에서 진행,
# 0, 0 에 위치, 뱀 길이 1, 방향은 오른쪽
# 몸길이를 ㄴ르려 ㄹ머리를 다음칸에 위치
# 이동한 칸에 사과 있으면, 사과 없어지고 꼬리 안움직임
# 사고 ㅏ업스면, 몸길이 줄여서 꼬리가 위치한 칸 비움, 몸길이 변하지 x
# 벽 or 자기자신과 부딪히면 게임 끝남
# 몇초에 게임이 끝나는지
t = 0
d = 0
hx, hy = 0, 0
arr[hx][hy] = 1
snake = deque()
snake.appendleft([hx, hy])
#사과면 10, 뱀이면 1, 빈칸 0

while True:
    t += 1
    nhx, nhy = hx+dx[d], hy+dy[d]
    if not (0<= nhx < n and 0<= nhy < n) or arr[nhx][nhy] == 1:

        break
    elif arr[nhx][nhy] == 10:#사과
        snake.appendleft([nhx, nhy])
        arr[nhx][nhy] = 1
        hx, hy = nhx, nhy
    else:#빈칸
        snake.appendleft([nhx, nhy])
        arr[nhx][nhy] = 1
        hx, hy = nhx, nhy
        x, y  = snake.pop()
        arr[x][y] = 0
    if t in dirs.keys():
        ex = dirs[t]
        if ex == 'L':
            d = (d-1)%4
        else:
            d = (d+1) % 4

print(t)
