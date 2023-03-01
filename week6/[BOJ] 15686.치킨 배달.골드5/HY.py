from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int , input().split())))
    
store = []
home = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            store.append((i,j))
        elif graph[i][j] == 1:
            home.append((i, j))
            
ans = 1e9

#치킨집 m개 모든 경우의 수
for case in combinations(store, m):
    d = 0
    for x, y in home:      #집마다 치킨집 최소 거리 구하기
        tmp = 1e9
        for a, b in case:
            tmp = min(tmp, abs(x - a) + abs(y - b))
        d += tmp
    ans = min(ans, d)
    
print(ans)