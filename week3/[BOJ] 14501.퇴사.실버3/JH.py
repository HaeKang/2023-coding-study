N = int(input())
T = [0]
P = [0] # numbering

max_profit = 0

def find(num, pro, last_picked): # 완전탐색으로 풀었어요
    global max_profit

    next = num + 1
    if next > N:
        max_profit = max(max_profit, pro)
        return

    # 선택한 경우
    if next >= last_picked + T[last_picked] and next + T[next] <= N+1:
        find(next, pro+P[next], next)
    # 선택하지 않는 경우
    find(next, pro, last_picked)

for i in range(N):
    t,p = map(int, input().split())
    T.append(t)
    P.append(p)

find(0,P[0],0)
print(max_profit)