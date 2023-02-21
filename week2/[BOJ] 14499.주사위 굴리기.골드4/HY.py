n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
direction = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]  #초기 주사위

def move(i):  #동,서,북,남 회전마다 주사위 숫자 변경
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if i == 1:
        dice[0] = d
        dice[1] = b
        dice[2] = a
        dice[3] = f
        dice[4] = e
        dice[5] = c
    elif i == 2:
        dice[0] = c
        dice[1] = b
        dice[2] = f
        dice[3] = a
        dice[4] = e
        dice[5] = d
    elif i == 3: 
        dice[0] = e
        dice[1] = a
        dice[2] = c
        dice[3] = d
        dice[4] = f
        dice[5] = b
    else: 
        dice[0] = b
        dice[1] = f
        dice[2] = c
        dice[3] = d
        dice[4] = a
        dice[5] = e
        
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for i in direction:
    nx = x + dx[i]
    ny = y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:    #graph 벗어나는 명령은 무시
        continue
    x, y = nx, ny
    move(i)
    if graph[x][y] == 0:
        graph[x][y] = dice[5]
    else:
        dice[5] = graph[x][y]
        graph[x][y] = 0
        
    print(dice[0])