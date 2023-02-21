N,L = map(int, input().split())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

bridge = []
for i in range(N):
    bridge.append([0] * N)

def put_bridge_h(pos):
    y, x = pos

    can_put = True
    if x + L < N:
        for i in range(1, L+1):
            if bridge[y][x+i] != 0 or area[y][x+i] != area[y][x] - 1:
                can_put = False
                break
        if can_put:
            for i in range(1, L+1):
                bridge[y][x+i] = -1

    can_put = True
    if x - L >= 0:
        for i in range(1, L+1):
            if bridge[y][x-i] != 0 or area[y][x-i] != area[y][x] - 1:
                can_put = False
                break
        if can_put:
            for i in range(1, L+1):
                bridge[y][x-i] = 1

def put_bridge_v(pos):
    y, x = pos

    can_put = True
    if y + L < N:
        for i in range(1, L+1):
            if bridge[y+i][x] != 0 or area[y+i][x] != area[y][x] - 1:
                can_put = False
                break
        if can_put:
            for i in range(1, L+1):
                bridge[y+i][x] = -1

    can_put = True
    if y - L >= 0:
        for i in range(1, L+1):
            if bridge[y-i][x] != 0 or area[y-i][x] != area[y][x] - 1:
                can_put = False
                break
        if can_put:
            for i in range(1, L+1):
                bridge[y-i][x] = 1

# def test_print():
#     for i in range(N):
#         print(' '.join(list(map(str, bridge[i]))))
#     print()

# 세로, 가로 따로 
# 경사로 놓을 수 있으면 놓고, 올라가는 것(+1)과 내려가는 것(-1)을 구분하여 마킹
# 갈 수 있는지 없는지 검사하기는 그냥 trial & error로 몇 번 시도해서 구현함 

cnt = 0
for i in range(N):
    # put bridge 
    for j in range(N):
        put_bridge_h((i,j))
    # check
    can_go = True
    for j in range(N-1):
        next = area[i][j+1]
        if next == area[i][j]:
            continue
        if next == area[i][j] + 1 and bridge[i][j] == 1:
            continue
        if next == area[i][j] - 1 and bridge[i][j+1] == -1:
            continue
        can_go = False
    if can_go:
        cnt += 1

#test_print()

# refresh bridge
bridge = []
for i in range(N):
    bridge.append([0] * N)


for j in range(N):
    # put bridge vertically
    for i in range(N):
        put_bridge_v((i,j))
    # check
    can_go = True
    for i in range(N-1):
        next = area[i+1][j]
        if next == area[i][j]:
            continue
        if next == area[i][j] + 1 and bridge[i][j] == 1:
            continue
        if next == area[i][j] - 1 and bridge[i+1][j] == -1:
            continue
        can_go = False
    if can_go:
        cnt += 1

print(cnt)