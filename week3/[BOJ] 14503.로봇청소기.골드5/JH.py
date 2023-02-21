## 실패 ##

# 시간을 많이 들이지 못했네요 ㅠㅠ

N,M = map(int, input().split())

start_y, start_x, current_dir = map(int, input().split())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

def test_print():
    for i in range(N):
        print(' '.join(list(map(str, area[i]))))
    print()


# 북 동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def operate(y, x):
    global current_dir, area

    area[y][x] = 2 # 청소 <- 뭔가 여기서 잘못된 것 같음..

    for i in range(4):   
        next_dir = current_dir - 1
        if next_dir < 0:
            next_dir = 3

        next_y = y + dy[next_dir]
        next_x = x + dx[next_dir]

        current_dir = next_dir
        if area[next_y][next_x] == 0:
            operate(next_y, next_x) # 1번으로

    else:
        next_y = y - dy[current_dir] # 후진
        next_x = x - dx[current_dir]

        if area[next_y][next_x] == 1: # 뒤가 벽인 경우
            return

        operate(next_y, next_x)

operate(start_y, start_x)

ret = 0
for i in range(N):
    for j in range(M):
        ret += int(area[i][j] == 2)

test_print()
print(ret)