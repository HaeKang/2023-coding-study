from collections import deque

N,K = map(int, input().split())
A = list(map(int, input().split()))
belt = deque()

for a in A:
    belt.append([a, 0]) # 벨트 내구도, 로봇 있음/없음

step = 0
while K > 0: # 주의: K > 0 조건을 달아야함
    step += 1

    # 벨트 회전
    belt.rotate(1)

    # 내려주기
    belt[N-1][1] = 0

    # 이동
    for i in range(N-2, -1, -1):
        if belt[i][1] == 1 and belt[i+1][1] == 0 and belt[i+1][0] >= 1:
            belt[i][1] = 0; belt[i+1][1] = 1
            belt[i+1][0] -= 1
            if belt[i+1][0] == 0: K -= 1 # K는 벨트 0의 수
    # 이동 후 내리기
    belt[N-1][1] = 0

    if belt[0][0] >= 1 and belt[0][1] == 0:
        belt[0][1] = 1
        belt[0][0] -= 1
        if belt[0][0] == 0: K -= 1

print(step)