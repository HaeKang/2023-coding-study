# reference: https://velog.io/@j_user0719/N으로-표현-PYTHON

def solution(N, number):
    answer = -1
    
    dp = []
    
    for i in range(1, 9): # i=1부터 8개까지 만들 수 있는 조합
        cand = set()
        cand.add(int(str(N) * i)) # N, NN, NNN, ...
        
        for j in range(0, i-1): # j개로 이전 것들의 조합으로 만들 수 있는 경우
            for op1 in dp[j]:
                for op2 in dp[-j-1]: # dp[3] = dp[1] op dp[2] + dp[2] op dp[1] 
                    cand.add(op1-op2)
                    cand.add(op1+op2)
                    cand.add(op1*op2)
                    if op2 != 0:
                        cand.add(op1 // op2)
    
        if number in cand: # i개로 만들 수 있으면 바로 return 
            return i

        dp.append(cand) # 아니면 i+1개로 넘어가기
    
    return answer