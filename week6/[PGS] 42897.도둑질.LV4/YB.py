def solution(money):
    n = len(money)
    dp = [0]*(n)
    dp[0] = money[0]
    dp[1] = max(money[0], money[1])
    dp[2] = max(dp[0]+money[2], dp[1])
    
    for i in range(2, n-1):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    
    answer =dp[-2]
    dp = [0]*(n)
    dp[1] = money[1]
    dp[2] = max(dp[0]+money[2], dp[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-2]+money[i], dp[i-1])
    
    answer = max(answer, dp[-1])
    
    return answer
