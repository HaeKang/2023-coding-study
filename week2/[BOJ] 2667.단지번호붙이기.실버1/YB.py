from collections import deque
n = int(input())
arr = []
for i in range(n):
    temp = input()
    arr.append([])
    for j in range(n):
        arr[i].append(int(temp[j]))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False]*n for _ in range(n)]

def find_house(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    cnt = 0
    while q:
        i, j = q.popleft()
        cnt += 1
        for d in range(4):
            ni, nj = i+dx[d], j+dy[d]
            if (0<= ni < n and 0<= nj < n):
                if not visited[ni][nj] and arr[ni][nj] == 1:
                    visited[ni][nj] = True
                    q.append([ni, nj])
    return cnt

danji_num = 0
house_cnt = []
for x in range(n):
    for y in range(n):
        if arr[x][y] > 0 and not visited[x][y]:
            danji_num +=1
            house_cnt.append(find_house(x, y))

print(danji_num)
for cnt in sorted(house_cnt):
    print(cnt)
