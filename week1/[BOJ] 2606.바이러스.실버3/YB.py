from collections import deque
def bfs(x):
    answer = 0
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        answer += 1
        now = q.popleft()
        for new in graph[now]:
            if not visited[new]:
                visited[new] = True
                q.append(new)
    return answer

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
visited[1] = True


print(bfs(1)-1)
