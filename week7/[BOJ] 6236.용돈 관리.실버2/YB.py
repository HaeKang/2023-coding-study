# m번만 돈 빼기
# k원 인출
# 남은 금액 다시 넣고 k원 인출
#

n, m = map(int, input().split())
costs = []
for _ in range(n):
    costs.append(int(input()))
st, end = 0, n*10000

max_cost = max(costs)
answer = float('inf')
while st<= end:
    k = (st+end)//2
    cnt = 1
    if k < max_cost:
        st = k+1
        continue
    money = k

    for i in range(n):
        if costs[i] <= money:
            money -= costs[i]
        else:
            cnt += 1
            money = k-costs[i]
    if cnt > m:
        st = k+1
    else:
        answer = min(answer, k)
        end = k-1
print(answer)
