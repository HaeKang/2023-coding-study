# 톱니바퀴 A 회전 회전 방식
# 1. 톱니바퀴 B와 맞닿은 극이 다르면 > B는 A랑 반대방향으로
# 2. 톱니바퀴 B와 맞닿은 극이 같으면 > 회전 x
import copy
tires = [[] for _ in range(4)]
for i in range(4):
    tires[i] = [int(s) for s in input()]

for o in range(int(input())):
    idx, d = map(int, input().split())
    idx -= 1
    #d 1이면 시계, -1 반시계

    # 2, -2 확인

    check = [0, 0, 0, 0]
    check[idx] = d
    for i in range(idx, 3):
        if check[i] != 0 and tires[i][2] != tires[i+1][-2]:
            check[i+1] = check[i]*(-1)
        else:
            break
    for i in range(idx, 0, -1):
        if check[i] != 0 and tires[i][-2] != tires[i-1][2]:
            check[i-1] = check[i]*(-1)
        else:
            break

    # 회전시키기
    for i in range(4):
        if check[i] == 0:
            continue
        elif check[i] == 1:
            temp = copy.deepcopy(tires[i])
            new = [temp[-1]] + temp[0:-1]
        else:
            temp = copy.deepcopy(tires[i])
            new = temp[1:] + [temp[0]]
        tires[i] = new

# N극은 0 S극은 1
score = 0
for i in range(4):
    if tires[i][0] == 1:
        score += (2**(i))
print(score)
