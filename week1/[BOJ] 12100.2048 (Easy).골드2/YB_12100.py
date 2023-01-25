# 12: 35
import copy

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 이동할때, arr에는 합치는 건 반영 x, 움직이는 것만 반영,
# 합쳐지면 해당칸을 그냥 0으로?
# new_arr == 지금 -> arr == 지금 면 합치기
# 안똑같으면 이동만
dx = [-1, 0, 1, 0]#위 오른 아래 왼
dy = [0, 1, 0, -1]

def move_up(arr):
    new_arr = copy.deepcopy(arr)
    for y in range(n):
        for x in range(1, n):
            if arr[x][y] == 0:
                continue
            nx = x
            now = copy.deepcopy(arr[x][y])
            check = False
            while 0<= nx-1 < n:
                if new_arr[nx-1][y] == 0:
                    nx -= 1
                elif new_arr[nx-1][y] == now and arr[nx-1][y] == now:
                    new_arr[nx-1][y] = 2*now
                    check = True
                    new_arr[x][y] = 0
                    arr[x][y] = 0
                    break
                else:
                    break
            if nx != x and not check:
                new_arr[nx][y] = now
                new_arr[x][y] = 0
                arr[nx][y] = now
                arr[x][y] = 0
    arr = new_arr
    return new_arr
def move_down(arr):
    new_arr = copy.deepcopy(arr)
    for y in range(n):
        for x in range(n-2, -1, -1):
            if arr[x][y] == 0:
                continue
            nx = x
            now = copy.deepcopy(arr[x][y])
            check = False
            while 0<= nx+1 < n:
                if new_arr[nx+1][y] == 0:
                    nx += 1
                elif new_arr[nx+1][y] == now and arr[nx+1][y] == now:
                    new_arr[nx+1][y] = 2*now
                    check = True
                    new_arr[x][y] = 0
                    arr[x][y] = 0
                    break
                else:
                    break
            if nx != x and not check:
                new_arr[nx][y] = now
                new_arr[x][y] = 0
                arr[nx][y] = now
                arr[x][y] = 0
    arr = new_arr
    return new_arr

def move_right(arr):
    new_arr = copy.deepcopy(arr)
    for x in range(n):
        for y in range(n-2, -1, -1):
            if arr[x][y] == 0:
                continue
            ny = y
            now = copy.deepcopy(arr[x][y])
            check = False
            while 0<= ny+1 < n:
                if new_arr[x][ny+1] == 0:
                    ny += 1
                elif new_arr[x][ny+1] == now and arr[x][ny+1] == now:
                    new_arr[x][ny+1] = 2*now
                    check = True
                    new_arr[x][y] = 0
                    arr[x][y] = 0
                    break
                else:
                    break
            if ny != y and not check:
                new_arr[x][ny] = now
                new_arr[x][y] = 0
                arr[x][ny] = now
                arr[x][y] = 0
    return new_arr
def move_left(arr):
    new_arr = copy.deepcopy(arr)
    for x in range(n):
        for y in range(1, n):
            if arr[x][y] == 0:
                continue
            ny = y
            now = copy.deepcopy(arr[x][y])
            check = False
            while 0<= ny-1 < n:
                if new_arr[x][ny-1] == 0:
                    ny -= 1
                elif new_arr[x][ny-1] == now and arr[x][ny-1] == now:
                    new_arr[x][ny-1] = 2*now
                    check = True
                    new_arr[x][y] = 0
                    arr[x][y] = 0
                    break
                else:
                    break
            if ny != y and not check:
                new_arr[x][ny] = now
                new_arr[x][y] = 0
                arr[x][ny] = now
                arr[x][y] = 0
    return new_arr

def dfs(arr, cnt):
    global answer
    if cnt >= 5:
        for x in range(n):
            answer = max(answer, max(arr[x]))
        return
    dfs(move_up(copy.deepcopy(arr)), cnt+1)
    dfs(move_down(copy.deepcopy(arr)), cnt+1)
    dfs(move_right(copy.deepcopy(arr)), cnt+1)
    dfs(move_left(copy.deepcopy(arr)), cnt+1)
    return
answer=  2
dfs(arr, 0)
print(answer)
