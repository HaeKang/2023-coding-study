# 8: 01
# 로봇은 올리는 위치에만
# 로봇이 내리는 위치 도달하면 즉시 내림
# 로봇은 스스로 이동 가능
# 로봇을 올리는 위치에 올리거나 어떤 칸으로 이동하면 내구도 -= 1
#

n, k = map(int, input().split())

power = list(map(int, input().split()))
robot = [False]*n
t = 1
st = 0

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전
   
    st = (st-1)%(2*n)
    robot = [False] + robot[:-1]
    robot[-1] = False
    # 2. 가장 먼저 벨트 올라간 로봇부터 한칸 이동 가능하면 이동
    #     이동하려는 칸에 로봇이 없고, 내구도가 1이상 남아있어야 함
    for i in range(n-2, -1, -1):
        if not robot[i]:
            continue

        if not robot[i+1] and power[(st+i+1)%(2*n)] >= 1:
            robot[i+1] = True
            robot[i] = False
            power[(st+i+1)%(2*n)] -= 1
    robot[-1] = False
    # 3. 올리는 위치에 있는 칸의 내구도가 0 < power 이면 로봇 올림
    if power[st] > 0:
        robot[0] = True
        power[st] -= 1

    # 4. power == 0인 칸 k 이상이면 종료
    cnt = 0
    for p in power:
        if p == 0:
            cnt += 1
    if cnt >= k:
        break
    t += 1
print(t)
