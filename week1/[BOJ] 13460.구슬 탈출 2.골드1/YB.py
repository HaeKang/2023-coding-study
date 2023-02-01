# 7:12
# 구멍 한개, 파란 구술이 구멍에 들어가면 안되며 빨간 구슬 빼기
# 동시에 구멍에 빠져도 실패
# 중력을 이용해 이리절 ㅣ굴리기
# 네방향, 공은 동시에 움직이고
# 기울이기 stop 조건: 더이상 구슬 움직이지 않을때까지
import copy
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([s for s in input()])

# 10번 넘으면 -1 출력->11부터는 -1 출력
answer = float('inf')
dx = [0, 1, 0, -1]#오 아래 왼 위
dy = [1, 0, -1, 0]

def gravity(d): # 기울이기 & 결과 체크0
    global my_arr
    Rcheck = False
    Bcheck = False
    cnt = 0
    if d == 0:#오 y +1 방향
        for x in range(n):
            for y in range(m-1, -1, -1):
                if my_arr[x][y] == 'R' or my_arr[x][y] == 'B':
                    ny = y
                    while (ny+1) < m:
                        if my_arr[x][ny+1] == '.' :
                            ny += 1
                        elif my_arr[x][ny+1] == 'O':
                            ny += 1
                            break
                        else:
                            break
                    cnt += abs(ny-y)

                    if my_arr[x][ny] == 'O':
                        if my_arr[x][y] == 'R':
                            my_arr[x][y] = '.'
                            Rcheck = True
                        else:
                            arr[x][y] = '.'
                            Bcheck = True
                    elif my_arr[x][ny] == '.':
                        my_arr[x][ny] = copy.deepcopy(my_arr[x][y])
                        my_arr[x][y] = '.'

    elif d == 1: #아래 x +1
        for y in range(m):
            for x in range(n-1, -1, -1):
                if my_arr[x][y] == 'R' or my_arr[x][y] == 'B':
                    nx = x
                    while (nx+1) < m:
                        if my_arr[nx+1][y] == '.' :
                            nx += 1
                        elif my_arr[nx+1][y] == 'O':
                            nx += 1
                            break
                        else:
                            break
                    cnt += abs(nx - x)
                    if my_arr[nx][y] == 'O':
                        if my_arr[x][y] == 'R':
                            my_arr[x][y] = '.'
                            Rcheck = True
                        else:
                            my_arr[x][y] = '.'
                            Bcheck = True
                    elif my_arr[nx][y] == '.':
                        my_arr[nx][y] = copy.deepcopy(my_arr[x][y])
                        my_arr[x][y] = '.'

    elif d == 2:#왼
        for x in range(n):
            for y in range(m):
                if my_arr[x][y] == 'R' or my_arr[x][y] == 'B':
                    ny = y
                    while (ny-1) >= 0:
                        if my_arr[x][ny-1] == '.':
                            ny -= 1
                        elif my_arr[x][ny-1] == 'O':
                            ny -= 1
                            break
                        else:
                            break
                    cnt += abs(ny - y)
                    if my_arr[x][ny] == 'O':
                        if my_arr[x][y] == 'R':
                            my_arr[x][y] = '.'
                            Rcheck = True
                        else:
                            my_arr[x][y] = '.'
                            Bcheck = True
                    elif my_arr[x][ny] == '.':
                        my_arr[x][ny] = copy.deepcopy(my_arr[x][y])
                        my_arr[x][y] = '.'

    else: # 위
        for y in range(m):
            for x in range(n):
                if my_arr[x][y] == 'R' or my_arr[x][y] == 'B':
                    nx = x
                    while (nx-1) >= 0:
                        if my_arr[nx-1][y] == '.' :
                            nx -= 1
                        elif my_arr[nx-1][y] == 'O':
                            nx -= 1
                            break
                        else:
                            break
                    cnt += abs(nx - x)
                    if my_arr[nx][y] == 'O':
                        if my_arr[x][y] == 'R':
                            my_arr[x][y] = '.'
                            Rcheck = True
                        else:
                            my_arr[x][y] = '.'
                            Bcheck = True
                    elif my_arr[nx][y] == '.':
                        my_arr[nx][y] = copy.deepcopy(my_arr[x][y])
                        my_arr[x][y] = '.'
    if cnt == 0:
        Bcheck = True
    return Rcheck, Bcheck
def dfs(t, arr):
    global my_arr, answer
    if t >= answer or t >= 10:
        return
    for d in range(4):
        my_arr = copy.deepcopy(arr)
        Rcheck, Bcheck = gravity(d)

        if not Rcheck and not Bcheck:
            dfs(t + 1, my_arr)
        elif Rcheck and not Bcheck:
            answer = min(answer, t+1)
    return

dfs(0, copy.deepcopy(arr))
if answer == float('inf'):
    answer = -1
print(answer)
