from collections import deque
def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for wire in wires:
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    def bfs(x):
        visited = [False for _ in range(n + 1)]
        q = deque()
        q.append(x)
        visited[x] = True
        cnt = 1
        #연결된 전선이 있는 경우 모두 탐색하며 count
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    cnt += 1

        return cnt
            
    answer = n
    for wire in wires:
        #하나씩 제거하면서 결과 확인
        graph[wire[0]].remove(wire[1])
        graph[wire[1]].remove(wire[0])
        
        answer = min(abs(bfs(wire[0]) - bfs(wire[1])), answer)
        #다시 추가
        graph[wire[0]].append(wire[1])
        graph[wire[1]].append(wire[0])
    
    return answer