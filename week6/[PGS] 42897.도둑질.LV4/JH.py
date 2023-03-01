def solution(money):
    ### 답 보고 제출: 첫 번째 포함하거나 하지 않거나로 나누어서 접근 ### 
    
    answer = 0
    n = len(money)
    
    dp1 = [0] * n
    dp2 = [0] * n
    
    dp1[0] = money[0] # 첫 번째를 선택함
    dp1[1] = max(money[1], dp1[0])
    
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-2] + money[i], dp1[i-1])
    
    dp2[0] = 0 # 첫 번째를 선택하지 않음
    dp2[1] = money[1]
    
    for i in range(2, n): # 마지막까지
        dp2[i] = max(dp2[i-2] + money[i], dp2[i-1])
    
    answer = max(max(dp1), max(dp2))
    return answer