import sys

N,M = map(int, input().split())

area = []
for i in range(N):
    area.append(sys.stdin.readline().rstrip().split())

def test_print():
    for i in range(N):
        print(' '.join(area[i]))
    print()

cctv = []
cctv_5 = []
for i in range(N):
    for j in range(M):
        if area[i][j] in '1234':
            cctv.append((i,j,area[i][j])) # y, x, type
        if area[i][j] == '5':
            cctv_5.append((i,j))

min_cnt = 65

def update():
    global min_cnt, area
    # 세보고 업데이트
    cnt = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] == '0':
                cnt += 1
    min_cnt = min(min_cnt, cnt)
    
    # 원상복구
    for i in range(N):
        for j in range(M):
            if area[i][j] == '#':
                area[i][j] = '0'

def light_N(pos):
    global area
    y, x = pos

    k = 1
    while(y-k >= 0 and area[y-k][x] != '6'):
        if area[y-k][x] == '0':
            area[y-k][x] = '#'
        k += 1

def light_S(pos):
    global area
    y, x = pos

    k = 1
    while(y+k < N and area[y+k][x] != '6'):
        if area[y+k][x] == '0':
            area[y+k][x] = '#'
        k += 1

def light_E(pos):
    global area
    y, x = pos

    k = 1
    while(x+k < M and area[y][x+k] != '6'):
        if area[y][x+k] == '0':
            area[y][x+k] = '#'
        k += 1

def light_W(pos):
    global area
    y, x = pos

    k = 1
    while(x-k >= 0 and area[y][x-k] != '6'):
        if area[y][x-k] == '0':
            area[y][x-k] = '#'
        k += 1


def light_5(pos):
    light_W(pos)
    light_E(pos)
    light_S(pos)
    light_N(pos)

# 0 1 2 3 
# 동 서 남 북
def light(pos, type, dir):
    if type == '1':
        if dir == 0:
            light_E(pos)
        elif dir == 1:
            light_W(pos)
        elif dir == 2:
            light_S(pos)
        else:
            light_N(pos)

    if type == '2':
        if dir == 0 or dir == 1:
            light_W(pos)
            light_E(pos)
        else:
            light_N(pos)
            light_S(pos)

    if type == '3':
        if dir == 0:
            light_E(pos)
            light_N(pos)
        elif dir == 1:
            light_N(pos)
            light_W(pos)
        elif dir == 2:
            light_W(pos)
            light_S(pos)
        else:
            light_E(pos)
            light_S(pos)

    if type == '4':
        if dir == 0:
            light_N(pos)
            light_W(pos)
            light_S(pos)
        elif dir == 1:
            light_E(pos)
            light_W(pos)
            light_S(pos)
        elif dir == 2:
            light_E(pos)
            light_N(pos)
            light_S(pos)
        else:
            light_E(pos)
            light_N(pos)
            light_W(pos)

dirs = []      
def decide_dirs():
    global area
    
    if len(dirs) == len(cctv): # 방향 정해진 경우
        for i in range(len(dirs)):
            dir = dirs[i]
            y, x, type = cctv[i]
            light((y,x), type, dir) # 1,2,3,4번 불켜기

        for tv in cctv_5:
            light_5(tv) # 5번 불켜기
        # test_print()
        update() # 업데이트 및 맵 원상 복구
        return
    
    
    for i in range(4):
        dirs.append(i)
        decide_dirs()
        dirs.pop() # 모든 경우 탐색, 최대 8^4 = 2^12

decide_dirs()
print(min_cnt)