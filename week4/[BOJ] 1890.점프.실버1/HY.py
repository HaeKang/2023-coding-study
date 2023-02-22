import sys
#input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
cnt = [[0] * n for _ in range(n)]
cnt[0][0] = 1   #출발 위치
        
for i in range(n):
    for j in range(n):
        # 마지막 칸도 count를 하기 때문에 break 해주기
        if i == n - 1 and j == n - 1:
            break
        if cnt[i][j] != 0:  #점프를 해서 갔으면
            if i + graph[i][j] < n:
                cnt[i + graph[i][j]][j] += cnt[i][j]   #새로운 칸에 cnt 더해주기
            if j + graph[i][j] < n:
                cnt[i][j + graph[i][j]] += cnt[i][j]
            
print(cnt[n - 1][n - 1])