import sys
#input = sys.stdin.readline

#재귀
def pooling(n, graph):
    if n == 1:
        print(graph[0][0])   # 결과가 [[17]] 형태여서 graph[0][0]으로 출력
        return
    new_graph = []
    for i in range(0, n, 2):
        arr = []
        for j in range(0, n, 2):
            tmp = []
            tmp.extend(graph[i][j : j + 2])
            tmp.extend(graph[i + 1][j : j + 2])
            tmp.sort()   #범위에 해당하는 (2,2) 값 중 2번째 큰 값으로 새로운 graph 만들기
            if len(tmp) != 1:
                arr.append(tmp[-2])
        new_graph.append(arr)
    pooling(len(new_graph), new_graph)
    
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
pooling(n, graph)