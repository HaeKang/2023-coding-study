from collections import deque

N = int(input())

town = []
for i in range(N):
    s = input()
    row = []
    for c in s:
        row.append(int(c))
    town.append(row)

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(start): # 단순한 bfs
    global town
    q = deque()
    q.append(start)
    town[start[0]][start[1]] = 0 # visit = 맵에서 그냥 0으로 만들기
    num = 1 # 집 세어주기

    while(q):
        current = q.popleft()

        for i in range(4):
            next_y, next_x = current[0]+dy[i], current[1]+dx[i]

            if next_y >= N or next_x >= N or next_y < 0 or next_x < 0:
                continue

            if town[next_y][next_x]:
                q.append((next_y,next_x))
                town[next_y][next_x] = 0 
                num += 1
    return num


cnt = 0
nums = []
for i in range(N):
    for j in range(N):
        if town[i][j]:
            nums.append(bfs((i,j)))
            cnt += 1

print(cnt)
nums.sort()
for n in nums:
    print(n)