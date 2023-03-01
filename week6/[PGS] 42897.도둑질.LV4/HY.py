def solution(money):
    #첫집을 안터는 경우
    dp1 = [0] * len(money)
    dp1[1] = money[1]
    for i in range(2, len(money)):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    #첫집 터는 경우
    dp2 = [0] * len(money)
    dp2[0] = money[0]
    dp2[1] = max(money[0], money[1])   #money = [90,0,0,95,1,1] ans = 185
    for i in range(2, len(money) - 1):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
    
    answer = max(max(dp1), max(dp2))
    return answer