import sys

N,M = map(int, input().split())

spend = []
for i in range(N):
    spend.append(int(sys.stdin.readline().rstrip()))

lo = max(spend)
hi = sum(spend)

while(lo <= hi):
    mid = (lo + hi) // 2

    rest = mid
    n = 1
    for m in spend:
        if rest < m: # 더 적으면 
            rest = mid  # 인출
            n += 1
        rest -= m # 남은 돈에서 spend 빼기

    if n > M: # 더 많이 인출한 경우
        lo = mid + 1
    else:  # M보다 적거나 같음 (인출 금액이 더 큼)
        hi = mid - 1
        k = mid # lower bound

print(k)