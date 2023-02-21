dx = [0, 1, 0, -1]# 오른 아래 왼 오
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
arr = []
cctv = []
for i in range(n):
    arr.append(list( map(int, input().split())))
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv.append([i,j, arr[i][j]])
answer = n*m




import copy
from collections import deque
def spread(x, y, arr, dirs):
    q = deque()
    for d in dirs:
        q.append([x, y, d])
    while q:
        x, y, d = q.popleft()
        nx, ny = x+dx[d], y+dy[d]
        if not (0<= nx < n and 0<= ny < m) or arr[nx][ny] == 6:
            continue
        arr[nx][ny] = -1
        q.append([nx, ny, d])

    return arr



def dfs(arr, cctv):
    global answer
    if not cctv:
        temp = 0
        for x in range(n):
            for y in range(m):
                if arr[x][y] == 0:
                    temp += 1

        answer = min(answer, temp)

        return
    new_cctv = copy.deepcopy(cctv)
    cx, cy, cnum = new_cctv.pop()
    if cnum == 1:
        ccnt, cdir = 4, [0]
    elif cnum == 2:
        ccnt, cdir = 2, [0, 2]
    elif cnum == 3:
        ccnt, cdir = 4, [0, 1]
    elif cnum == 4:
        ccnt, cdir = 4, [0, 1, 2]
    elif cnum == 5:
        ccnt, cdir = 1, [0, 1, 2, 3]

    for i in range(ccnt): #방향 회전
        new_arr = copy.deepcopy(arr)
        new_cdir = [(d+i)%4 for d in cdir]
        new_arr = spread(cx, cy, new_arr, new_cdir)
        dfs(new_arr, new_cctv)
    return



dfs(arr, cctv)
print(answer)
