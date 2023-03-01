
# 틀린코드
import copy
def ShiftRow(arr):
    arr = [arr[-1]] + arr[:-1]
    return arr

def rotate(now):
    global n, m
    new = copy.deepcopy(now)
    temp = now[:2*n+2*m-5]
    new[0] = now[2*n+2*m-5]
    new[1:2*n+2*m-5] = temp
    return new

def make_1d(arr):
    global n, m
    new = arr[0]
    l = [m-1, n-1]
    d = 1
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, m-1
    while not (x == n//2 and y == (n//2-1)):
        for _ in range(l[d%2]):
            x, y = x+dx[d], y+dy[d]
            new.append(arr[x][y])
        l[d%2] -= 1
        d = (d+1)%4
    return new

def solution(rc, ops):
    global n, m
    answer = [[]]
    
    n, m = len(rc), len(rc[0])

    now = make_1d(rc)
    print(now)
    print(rotate(now))
    return rc
