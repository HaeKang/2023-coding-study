from collections import deque


def bfs(node, graph, n):
    checked = [0] * (n+1)

    q = deque()
    q.append(node)
    checked[node] = 1
    cnt = 1

    while q:
        nx = q.popleft()
        for i in graph[nx]:
            if checked[i] == 0:
                q.append(i)
                checked[i] = 1
                cnt += 1
    return cnt


def solution(n, wires):
    answer = 1e9

    graph = [[] for _ in range(n+1)]
    for wire in wires:
        v1 = wire[0]
        v2 = wire[1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    for wire in wires:
        a = wire[0]
        b = wire[1]

        graph[a].remove(b)
        graph[b].remove(a)

        answer = min(abs(bfs(a, graph, n) - bfs(b, graph, n)), answer)

        graph[a].append(b)
        graph[b].append(a)

    return answer
