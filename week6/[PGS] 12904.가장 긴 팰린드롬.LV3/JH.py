def solution(s):
    answer = 0
    
    # 기준이 1개 ex. aabaa
    n = len(s)
    k = 0
    while(k < n):
        i = 0
        while(k-i >= 0 and k+i < n and s[k-i] == s[k+i]):
            i += 1
        answer = max(answer, 2*(i-1)+1)
        
        k += 1
    
    # 기준이 2개 ex. aabbcc
    k = 0
    while(k+1 < n):
        i = 0
        while(k-i >= 0 and k+1+i < n and s[k-i] == s[k+1+i]):
            i += 1
        answer = max(answer, 2*i) 
        
        k += 1
    
    return answer