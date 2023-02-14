n = int(input())
t = []
p = []
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    
dp = [0] * n  

for i in range(n):
    k = i + t[i] - 1  #상담완료 날짜
    if k >= n: # 범위 넘어가면 무시
        continue
    if i == 0: #out of index 발생해서 따로 처리
        dp[k] = p[0]
    else:      #상담 안했을 경우 최대와 지금까지 최대 + 상담한 경우 비교
        dp[k] = max(dp[k], max(dp[:i]) + p[i])

print(max(dp))