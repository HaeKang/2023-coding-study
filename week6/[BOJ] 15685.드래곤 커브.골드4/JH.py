## 규칙을 보고 풀었음 ##
import copy

N = int(input())
M = 101

area = []
for i in range(M):
    area.append([0] * M)

# 동 북 서 남
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def dragon_curve(x,y,d,g):

    def draw(dir, x, y):
        area[y][x] = 1
        end_y, end_x = y+dy[dir], x+dx[dir]
        area[end_y][end_x] = 1
        return end_x, end_y

    dirs = []
    for k in range(g+1):
        if len(dirs) < 1:
            dirs.append(d)
        else:
            temp = copy.deepcopy(dirs)
            while(temp):
                dirs.append((temp.pop() + 1) % 4) # 규칙: 스택으로 이전 것 (d+1) // 4
    for dir in dirs:
        x, y = draw(dir, x, y)

for i in range(N):
    x,y,d,g = map(int, input().split())
    dragon_curve(x,y,d,g)

# print()
# for i in range(6):
#     print(area[i][:6])
# print()

cnt = 0
for i in range(M-1):
    for j in range(M-1):
        cnt += int(area[i][j] == 1 and area[i+1][j] == 1 and area[i][j+1] == 1 and area[i+1][j+1] == 1)
print(cnt)