import copy

n, m, x, y, k = map(int, input().split())
orders = []

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
dice = [0]*6

def move(d):
    global dice
    new_dice = copy.deepcopy(dice)
    if d == 3:
        new_dice[0], new_dice[2], new_dice[4], new_dice[5] = dice[5], dice[0], dice[2], dice[4]
    elif d == 4:
        new_dice[0], new_dice[2], new_dice[4], new_dice[5] = dice[2], dice[4], dice[5], dice[0]
    elif d == 1:
        new_dice[0], new_dice[1], new_dice[3], new_dice[4] = dice[1], dice[4], dice[0], dice[3]
    else:
        new_dice[0], new_dice[1], new_dice[3], new_dice[4] = dice[3], dice[0], dice[4], dice[1]
    dice = copy.deepcopy(new_dice)
    return

dx = [0, 0, 0, -1, 1]#오른, 왼, 위, 아래
dy = [0, 1, -1, 0, 0]
for d in map(int, input().split()):
    nx, ny = x+dx[d], y+dy[d]
    if not (0<= nx < n and 0<= ny < m):
        continue
    x, y = nx, ny
    move(d)
    if arr[x][y] == 0:
        arr[x][y] = dice[4]
    else:
        dice[4] = arr[x][y]
        arr[x][y] = 0
    print(dice[0])
