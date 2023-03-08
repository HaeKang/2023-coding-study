import copy
from collections import deque
def check_num(v):
    global visited, graph
    q = deque()
    q.append(v)
    visited[v] = True
    num = 0
    while q:
        num +=1
        x = q.popleft()
        for new in graph[x]:
            if not visited[new]:
                visited[new] = True
                q.append(new)
    return num
    
def solution(n, wires):
    global graph, visited
    
    answer = float('inf')
    
    for i in range(n-1):
        now_wires = copy.deepcopy(wires)
        now_wires = now_wires[:i] + now_wires[i+1:]
        graph = [[] for _ in range(n+1)]
        for i in range(n-2):
            v1, v2 = now_wires.pop()
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = [False]*(n+1)
        for v in range(1, n+1):
            if not visited[v]:
                num1 = check_num(v)

        answer = min(abs(n-num1*2), answer)

    return answer       
