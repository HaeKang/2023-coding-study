'''
틀린코드..왜 틀렸는지 모르겠음
'''

import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
arr_copy = [[5 for _ in range(n)] for _ in range(n)]

trees = [[deque() for _ in range(n)]  for _ in range(n)] # 산 나무

for _ in range(m):
    tree_r, tree_c, tree_old = map(int, input().split())
    trees[tree_r-1][tree_c-1].append(tree_old)


# 8가지 방향 (x:row, y:col)
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

# 봄
def spring(dead_trees):

    for i in range(n):
        for j in range(n):
            # 나무가 있으면
            if len(trees[i][j]) > 0:
                sorted(trees[i][j])   # 나이순으로 정렬
                
                for _ in range(len(trees[i][j])):
                    now_old = trees[i][j].popleft()

                    if arr_copy[i][j] >= now_old:
                        arr_copy[i][j] -= now_old
                        now_old += 1
                        trees[i][j].append(now_old)
                    
                    else:
                        dead_trees[i][j].append(now_old)

    return dead_trees

# 여름 가을 겨울 
def other_season(dead_trees):
    for i in range(n):
        for j in range(n):
            # 여름
            if len(dead_trees[i][j]) > 0:
                while dead_trees[i][j]:
                    arr_copy[i][j] += dead_trees[i][j].popleft() // 2
            
            # 가을
            if len(trees[i][j]) > 0:
                for _ in range(len(trees[i][j])):
                    now_old = trees[i][j].popleft()
                    trees[i][j].append(now_old)

                    # 5의 배수이면
                    if now_old % 5 == 0:
                        for k in range(8):
                            nr = i + dr[k]
                            nc = j + dc[k]

                            if 0 <= nr < n and 0<= nc < n:
                                trees[nr][nc].append(1)
            
            # 겨울
            arr_copy[i][j] += arr[i][j]


def print_board(tmp):
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            print(tmp[i][j], end=" ")
        print()


# k년
for _ in range(k):
    dead_trees = [[deque() for _ in range(n)] for _ in range(n)]    # 죽은 나무
    
    # 봄
    dead_trees = spring(dead_trees)

    # 여름 가을 겨울
    other_season(dead_trees)

ans = 0
for i in range(n):
    for j in range(n):
        if len(trees[i][j]) > 0:
            ans += len(trees[i][j])

print(ans) 