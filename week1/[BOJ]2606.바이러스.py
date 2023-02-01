import queue

N = int(input())
M = int(input())
edges = []
for i in range(M):
    edges.append(tuple(map(int, input().split())))

cnt = 0

q = queue.Queue() # BFS
q.put(1)
visited = [1]
while(q.qsize()>=1):
    current = q.get()

    for i,j in edges:

        if i != current and j != current:
            continue

        if i == current: 
            next = j
        if j == current: # 양방향 edge
            next = i

        if next not in visited:
            visited.append(next)
            q.put(next)
            cnt += 1

print(cnt)