## 최소 신장 트리, 크루스칼 알고리즘

def find_parent(parent, i):
    if i != parent[i]:
        parent[i] = find_parent(parent, parent[i]) # i 노드의 parent는 조상
    return parent[i]


def union_parent(parent, i, j):
    parent_i = find_parent(parent, i)
    parent_j = find_parent(parent, j)
    
    if parent_i < parent_j: # 작은 쪽이 부모가 되도록
        parent[parent_j] = parent_i 
    else:
        parent[parent_i] = parent_j
        

def solution(n, costs):
    answer = 0
        
    costs = sorted(costs, key=lambda x : x[2]) # cost가 낮은 순으로 정렬
    parent = [i for i in range(n)]
    
    for i,j,c in costs:

        if find_parent(parent, i) != find_parent(parent, j): # union-find 알고리즘
            union_parent(parent, i, j)
            answer += c
    return answer