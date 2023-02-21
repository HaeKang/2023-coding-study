#import copy

N = int(input())

S = []
for i in range(N):
    S.append(list(map(int, input().split())))

ret = 1E+10

def calculate(array):
    score = 0
    k = len(array)
    for i in range(k):
        for j in range(i+1, k):
            score += S[array[i]][array[j]] + S[array[j]][array[i]]
    return score


def select(array):
    global N, S, ret

    if len(array) == N//2:

        not_in = []
        for i in range(N):
            if i not in array:
                not_in.append(i)

        score_start = calculate(array)
        score_link = calculate(not_in)

        ret = min(ret, abs(score_link-score_start))
        return

    for i in range(N):
        cp_array = array #copy.deepcopy(array)
        if len(cp_array) == 0 or cp_array[-1] < i:
            cp_array.append(i)
            select(cp_array)
            cp_array.pop() # DFS

select([])
print(ret)