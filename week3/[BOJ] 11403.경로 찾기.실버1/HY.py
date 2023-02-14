
#3중 포문을 돌아야해서 시간 복잡도는 O(n^3)이다
#주의할 점은 3중 포문 중 경로가 되는 k의 포문이 가장 위에 있어야 누락하지 않고 한번에 돌 수 있다

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
                
for a in range(n):
    for b in range(n):
        print(graph[a][b], end = ' ')
    print()