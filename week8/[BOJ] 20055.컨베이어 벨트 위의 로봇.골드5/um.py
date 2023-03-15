import sys
# python 시간 초과 pypy 통과
in_d = sys.stdin.readline
N, K = list(map(int, in_d().split()))
Ai = list(map(int, in_d().split()))
rob = [False] * N
t = 1

while True:
    # 1. turn
    Ai = [Ai[-1]] + Ai
    rob = [False] + rob
    del Ai[-1], rob[-1]
    rob[-1] = False
    # 2. move
    for kka in range(N-2,0,-1):
        if rob[kka] and (not rob[kka+1]) and Ai[kka+1] > 0:
            rob[kka+1] = True
            Ai[kka+1] -= 1
            rob[kka] = False

    # 3. on
    if Ai[0] > 0:
        rob[0] = True
        Ai[0] -= 1

    # 4. end
    cnt = 0
    for kka in range(2*N):
        if Ai[kka] == 0:
            cnt += 1
    if cnt >= K :
        break
    t += 1

print(t)