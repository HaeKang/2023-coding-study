'''
크루스칼
'''
# 부모 노드 찾기
def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    
    return parent[node]

# 연결
def union(parent, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2
    
    return parent

def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(0, n+1)] # 부모노드
    costs.sort(key = lambda x : x[2])   # cost에 따라 정렬

    for cost in costs:
        n1 = cost[0]
        n2 = cost[1]
        c = cost[2] # 비용

        if find(parent, n1) != find(parent, n2):
            parent = union(parent, n1, n2)
            answer += c
    
    return answer
