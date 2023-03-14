R,C,T = map(int, input().split())

area = []
for i in range(R):
    area.append(list(map(int, input().split())))

cond = []
for i in range(R):
    for j in range(C):
        if area[i][j] == -1:
            cond.append((i,j))

# def test_print():
#     for i in range(R):
#         print(' '.join(list(map(str, area[i]))))
#     print()

dy = [1,-1,0,0]
dx = [0,0,-1,1]
def spread():
    global area
    original = [[0] * C for i in range(R)]

    for i in range(R):
        for j in range(C):
            if area[i][j] > 0:
                original[i][j] = 1 # 확산되기 전 미세먼지들을 표시

    apply_spread = []
    apply_reduce = []
    for i in range(R):
        for j in range(C):
            if original[i][j] <= 0:
                continue

            count = 0
            for d in range(4):
                next_y = i + dy[d]
                next_x = j + dx[d]
                if next_y < R and next_y >= 0 and next_x < C and next_x >= 0 and area[next_y][next_x] != -1:
                    count += 1
                    apply_spread.append((next_y, next_x, area[i][j] // 5)) # 확산할 양을 저장
            apply_reduce.append((i,j,(area[i][j] // 5) * count)) # 줄어들 양을 저장 (이렇게 안하면 동시 확산을 구현하지 못함)

    for y,x,v in apply_spread:
        area[y][x] += v
    for y,x,v in apply_reduce:
        area[y][x] -= v

up_y, up_x = cond[0]
down_y, down_x = cond[1]

def blow():

    # 미세먼지 윗단
    temp = area[up_y][C-1]
    for x in range(C-2, 0, -1):
        area[up_y][x+1] = area[up_y][x]
    area[up_y][up_x+1] = 0

    temp2 = area[0][C-1]
    for y in range(1, up_y):
        area[y-1][C-1] = area[y][C-1]
    area[up_y-1][C-1] = temp

    temp = area[0][0]
    for x in range(1, C-1):
        area[0][x-1] = area[0][x]
    area[0][C-2] = temp2

    for y in range(up_y-2, 0, -1):
        area[y+1][0] = area[y][0]
    area[1][0] = temp

    # 미세먼지 아랫단
    temp = area[down_y][C-1]
    for x in range(C-2, 0, -1):
        area[down_y][x+1] = area[down_y][x]
    area[down_y][down_x+1] = 0

    temp2 = area[R-2][C-1]
    for y in range(R-3, down_y, -1):
        area[y+1][C-1] = area[y][C-1]
    area[down_y+1][C-1] = temp

    temp = area[R-1][1]
    for x in range(2, C):
        area[R-1][x-1] = area[R-1][x]
    area[R-1][C-1] = temp2

    for y in range(down_y+1, R-1):
        area[y][0] = area[y+1][0]
    area[R-1][0] = temp


while(T > 0):
    spread()
    blow()

    T -= 1

cnt = 0
for i in range(R):
    for j in range(C):
        if area[i][j] > 0:
            cnt += area[i][j]
print(cnt)