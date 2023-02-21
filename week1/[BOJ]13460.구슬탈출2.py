## 실패 ##

import queue

N,M = map(int, input().split())

map = []
for i in range(N):
    map.append(input())


visited = []
q = queue.Queue()

red_y, red_x, blue_y, blue_x = (0,0,0,0)
for i in range(N):
    for j in range(M):
        if map[i][j] == 'R':
            red_y, red_x = i,j
        if map[i][j] == 'B':
            blue_y, blue_x = i,j

q.put((red_y,red_x,blue_y,blue_x))
visited.append((red_y,red_x,blue_y,blue_x))

move_y = [-1, 1, 0, 0]
move_x = [0, 0, -1, 1]

def move(y, x, dy, dx):
    # 끝까지
    k = 0
    while(map[y+dy*k][x+dx*k] != 'O' and map[y+dy*k][x+dx*k] != '#'):
        k += 1

    if map[y+dy*k][x+dx*k] == '#': # 벽이면 전까지
        return y+dy*(k-1), x+dx*(k-1)

    return y+dy*k, x+dx*k

cnt = 0
red_in = False
blue_in = False

while(q.qsize() >= 1):

    if red_in or blue_in:
        if blue_in:
            cnt = -1
        break

    if cnt >= 10:
        #print('cnt over')
        cnt = -1
        break

    red_y, red_x, blue_y, blue_x = q.get()

    for i in range(4):
        dy, dx = move_y[i], move_x[i]

        next_red_y, next_red_x = move(red_y, red_x, dy, dx)
        next_blue_y, next_blue_x = move(blue_y, blue_x, dy, dx)

        print(next_red_y, next_red_x )

        if map[next_blue_y][next_blue_x] == 'O':
            cnt = -1
            blue_in = True
            break

        if map[next_red_y][next_red_x] == 'O':
            red_in = True
            cnt += 1
            break

        # 같은 경우 위치 조정
        if next_red_y == next_blue_y and next_red_x == next_blue_x:
            if dy == -1: # 상
                if red_y < blue_y:
                    next_blue_y += 1
                else:
                    next_red_y +=1
            if dy == 1: # 하
                if red_y < blue_y:
                    next_red_y -= 1
                else:
                    next_blue_y -= 1
            if dx == -1:
                if red_x < blue_x:
                    next_blue_x += 1
                else:
                    next_red_x += 1
            if dx == 1: # 우
                if red_x < blue_x:
                    next_red_x -= 1
                else:
                    next_blue_x -= 1

        next = (next_red_y, next_red_x, next_blue_y, next_blue_x)
        if next not in visited:
            q.put(next)

    cnt += 1

print(cnt)