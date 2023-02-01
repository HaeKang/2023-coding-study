from collections import deque

n = int(input())
apple = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(apple):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1

dir_dict = dict()
dir_num = int(input())
for _ in range(dir_num):
    a, b = input().split()
    dir_dict[int(a)] = b

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

direction = 0


def turn(x):
    global direction
    if x == "D":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4


q = deque()
q.append((0, 0))
arr[0][0] == 2
time = 0
x = 0
y = 0

while True:
    time += 1
    x = x + dx[direction]
    y = y + dy[direction]

    if x < 0 or x >= n or y < 0 or y >= n:
        break

    if arr[x][y] == 1:
        arr[x][y] = 2
        q.append((x, y))
        if time in dir_dict:
            turn(dir_dict[time])
    elif arr[x][y] == 0:
        arr[x][y] = 2
        q.append((x, y))
        a, b = q.popleft()
        arr[a][b] = 0
        if time in dir_dict:
            turn(dir_dict[time])
    else:
        break

print(time)