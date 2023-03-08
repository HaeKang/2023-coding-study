n, m, k = map(int, input().split())
balls = []
for _ in range(m):
    balls.append(list(map(int, input().split())))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

graph = [[[] for _ in range(n)] for _ in range(n)]
for r, c, m, s, d in balls:
        graph[r - 1][c - 1].append((m, s, d))

for i in range(k):
    new_graph = [[[] for _ in range(n)] for _ in range(n)]  # 이동후 결과 담을 graph
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                for m, s, d in graph[i][j]:
                    r, c = i, j
                    r += dx[d] * s  # d 방향으로 s만큼 이동 - 넘어가는 경우 고려
                    r %= n        
                    c += dy[d] * s
                    c %= n
                    new_graph[r][c].append((m, s, d)) 

    # 2개 이상일 경우 변환
    for r in range(n):
        for c in range(n):
            if len(new_graph[r][c]) > 1:
                sum_m = 0
                sum_s = 0
                odd = 0
                even = 0
                for m, s, d in new_graph[r][c]:
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        even += 1
                    else:
                        odd += 1
                if odd and even:  # 모두 짝수나 홀수가 아닌 경우
                    d = [1, 3, 5, 7]
                else:
                    d = [0, 2, 4, 6]
                tmp = []
                if int(sum_m/5) != 0:  #0일경우 파이어볼 제거
                    for i in range(4):
                        tmp.append((int(sum_m/5), int(sum_s/len(new_graph[r][c])), d[i]))

                new_graph[r][c] = tmp

    graph = new_graph

ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            for m, s, d in graph[i][j]:
                ans += m
print(ans)