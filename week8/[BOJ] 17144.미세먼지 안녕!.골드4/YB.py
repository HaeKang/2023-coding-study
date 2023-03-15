r, c, t = map(int, input().split())

arr = []
machine = []
for i in range(r):
    temp = list(map(int, input().split()))
    for j in range(c):#항상 1번 열에 설치되어 있고,
        if temp[j] == -1:
            machine.append(i)
    arr.append(temp)




# 1초동안 아래 일 발생
# 1. 미세먼지 확산 >> 동시에 일어남
#   인접한 네방향, Arc//5만큼 확산
#    공기청정기 있거나, 칸 범위 넘어가면 확산 x
#    남은 양은 Arc - (arc//5)x개수


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def spread_dust(arr):
    new_arr = copy.deepcopy(arr)

    for x in range(r):
        for y in range(c):
            if arr[x][y] == -1:
                continue
            ex_dust = arr[x][y]//5
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if 0<= nx < r and 0<= ny < c and arr[nx][ny] != -1:
                    new_arr[nx][ny] += ex_dust
                    new_arr[x][y] -= ex_dust
    return new_arr


# 2. 공기청정기 작동
#    바람이 나옴, 위쪽은 반시계방향으로 순환, 아래는 시계방향 순환
#    바람 불면 방향대로 모두 한칸씩 이동
#    공기청정기로 들어간 미세먼지는 모두 정화됨
def clean_room(arr):
    mx1, mx2 = machine
    new_arr = copy.deepcopy(arr)

    x, y, d = mx1, 1, 0
    new_arr[mx1][1] = 0
    #첫번째방향
    for _ in range(c-2):

        new_arr[x][y+1] = arr[x][y]
        y += 1

    #두번째방향
    for _ in range(mx1):
        new_arr[x-1][y] = arr[x][y]
        x -= 1

    # 세번째 방향
    for _ in range(c-1):

        new_arr[x][y-1] = arr[x][y]
        y -= 1

    # 네번째 방향
    for _ in range(mx1):

        new_arr[x+1][y] = arr[x][y]
        x += 1

    new_arr[mx1][0] = -1


    x, y, d = mx2, 1, 0
    new_arr[mx2][1] = 0
    # 첫번째방향
    for _ in range(c - 2):
        new_arr[x][y + 1] = arr[x][y]
        y += 1

    # 두번째방향
    for _ in range(r-mx2-1):
        new_arr[x+1][y] = arr[x][y]
        x += 1

    # 세번째 방향
    for _ in range(c-1):
        new_arr[x][y-1] = arr[x][y]
        y -= 1

    # 네번째 방향
    for _ in range(r-mx2-1):
        new_arr[x-1][y] = arr[x][y]
        x-= 1

    new_arr[mx2][0] = -1

    return new_arr
# t 초 지난후 남아있는 미세먼지 양
for _ in range(t):
    arr = spread_dust(arr)
    arr = clean_room(arr)


answer = 0
for x in range(r):
    for y in range(c):
        answer += arr[x][y]

print(answer+2)
