## 시간 초과! ##

def solution(number, k):
    answer = ''
    n = len(number) - k
    last_idx = -1
    
    while(n):
        
        s = number[last_idx+1:len(number)-n+1]  # 반대로 가장 큰 것들을 모으는 코드인데, O(n^2)라 시간초과..
        c = max(s)
        i = last_idx + 1 + s.index(c)
         
        answer += c
        last_idx = i
        
        n -= 1
    
    return answer