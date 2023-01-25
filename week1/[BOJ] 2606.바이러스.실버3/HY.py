ans = []


def dfs(v):
    visited[v] = 1
    ans.append(v)
    for i in range(1, n + 1):
        if visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


n = int(input())
m = int(input())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(1)
print(len(ans) - 1)