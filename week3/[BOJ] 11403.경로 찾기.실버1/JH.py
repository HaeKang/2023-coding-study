import copy

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

output = copy.deepcopy(graph) # 연결된 경로는 모두 방문 가능
visited = [0] * N

def dfs(i):
    for j in range(N):
        if graph[i][j]:
            output[i][j] = 1 # 순환 고려
            if not visited[j]:
                visited[j] = 1
                dfs(j)

for i in range(N):
    visited = [0] * N # 초기화
    dfs(i) # 각 node마다 dfs 돌려서 연결 관계 파악
    output[i] = visited # visited가 방문한 노드임

# 출력
for i in range(N):
    print(' '.join(list(map(str, output[i]))))