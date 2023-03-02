def solution(stc):
    answer = 1
    n = len(stc)
    for i in range(n):
        for j in range(i+1, n):
            if stc[i:j+1] == stc[i:j+1][::-1]:
                answer = max(answer, j-i+1)
    return answer
