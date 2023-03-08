import copy

def solution(n, wires):
    answer = n
    
    arr = [([0] * n) for i in range(n)] # graph
    
    for i,j in wires:
        arr[i-1][j-1] = arr[j-1][i-1] = 1
        
    for i,j in wires:
        copied = copy.deepcopy(arr)
        copied[i-1][j-1] = copied[j-1][i-1] = 0 # 잘라보고
        answer = min(answer, search(copied)) # 업데이트
    
    return answer


def search(copied):
    n = len(copied)
    visited = [0] * n
    
    ret = -1
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(i, copied, visited)
            if ret < 0: ret = sum(visited)
    ret = abs(ret - (n-ret)) # 트리 하나, 나머지 트리 하나
    return ret


def dfs(i, copied, visited):
    for j in range(len(copied)):
        if copied[i][j] and not visited[j]:
            visited[j] = 1
            dfs(j, copied, visited)