from itertools import combinations
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

a = [i for i in range(n)]
ans = 1e9  #최소값 확인용

for cases in combinations(a, n//2):  #0 ~ n 에서 절반 뽑는 모든 경우 확인
    visited = [False] * n
    for num in cases:       #뽑힌 수는 방문처리
        visited[num] = True
    start, link = 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if visited[i] and visited[j]:            #2개 다 방문했으면 start 아니면 link 팀으로 구분
                start += graph[i][j]
                start += graph[j][i]
            elif not visited[i] and not visited[j]:
                link += graph[i][j]
                link += graph[j][i]
                
    ans = min(ans, abs(start - link))
print(ans)