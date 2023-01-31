n = int(input())
line_cnt = int(input())

checked = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(line_cnt):
    v1, v2 = map(int, input().split(" "))
    graph[v1].append(v2)
    graph[v2].append(v1)


def dfs(node):
    checked[node] = 1
    for n in graph[node]:
        if checked[n] == 0:
            checked[0] += 1
            dfs(n)


dfs(1)
print(checked[0])
