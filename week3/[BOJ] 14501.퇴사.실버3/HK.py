n = int(input())
t = []
p = []
dp = [0] * (n+1)    # idx : 일자-1 | 해당 일자에 최대 이득

for _ in range(n):
    t1, p1 = map(int, input().split())
    t.append(t1)
    p.append(p1)

for i in range(n-1, -1, -1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1])

print(dp[0])
