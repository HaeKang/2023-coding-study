N,M,y,x,K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

dirs = list(map(int, input().split()))

W = [0] * 4 # 왼, 위, 오른, 바닥
H = [0] * 4 # 왼, 위, 오른, 바닥

def move(dir):
    global W, H

    if dir == 1: # 동
        memo = W[3]
        for i in range(3,0,-1):
            W[i] = W[i-1]
        W[0] = memo
        H[1] = W[1]
        H[3] = W[3]

    elif dir == 2: # 서
        memo = W[0]
        for i in range(0,3):
            W[i] = W[i+1]
        W[3] = memo
        H[1] = W[1]
        H[3] = W[3]
    
    elif dir == 3: # 북
        memo = H[0]
        for i in range(0, 3):
            H[i] = H[i + 1]
        H[3] = memo
        W[1] = H[1]
        W[3] = H[3]

    else: # 남
        memo = H[3]
        for i in range(3,0,-1):
            H[i] = H[i-1]
        H[0] = memo
        W[1] = H[1]
        W[3] = H[3]


def adapt(next):
    global arr, W, H
    
    map_val = arr[next[0]][next[1]]
    
    if map_val == 0:
        arr[next[0]][next[1]] = W[-1] # 바닥
    else:
        arr[next[0]][next[1]] = 0
        W[-1] = H[-1] = map_val


dy = [0,0,-1,1] # 동 서 북 남
dx = [1,-1,0,0]

for dir in dirs:

    next_y, next_x = y + dy[dir-1], x + dx[dir-1]

    if next_y >= N or next_x >= M or next_y < 0 or next_x < 0:
        continue

    move(dir) # 주사위 굴리기
    adapt((next_y, next_x)) # 현재 주사위의 바닥면 흡수 / 방출

    print(W[1])

    y, x = next_y, next_x # 다음 스텝