def solution(number, k):
    answer = []
    
    #k가 아직 있는데 더 큰 수가 나오는 경우 계속 제거
    for i in number:
        while  k > 0 and len(answer) != 0 and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)
        
    if k == 0:
        return ''.join(answer)
    else:
        return ''.join(answer[:-k])