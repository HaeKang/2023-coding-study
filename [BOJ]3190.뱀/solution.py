import sys
limit_number = 100*100
sys.setrecursionlimit(limit_number)

N = int(input())
K = int(input())

apples = []
for k in range(K):
    i, j = tuple(map(int, input().split()))
    apples.append((i-1,j-1))

L = int(input())
moves = []
for i in range(L):
    t, dir = input().split()
    t = int(t)
    moves.append((t, dir))

dy = [-1,1,0,0]
dx = [0,0,-1,1]

current_dir = 3 # right

cnt = 0 # sec
tails = [] # tail locations
k = 0 # moves_index

L_rot = 3,0,2,1
D_rot = 3,1,2,0
def get_next_dir(current_dir, move_sign):
    arr = L_rot
    if move_sign == 'D':
        arr = D_rot

    for i, k in enumerate(arr):
        if current_dir == k:
            return arr[(i+1) % 4]

def move(head): # 재귀 이용
    global cnt, tails, N, k, current_dir

    cnt += 1

    i, j = head
    next_head = i+dy[current_dir], j+dx[current_dir] # 다음 머리
    next_i, next_j = next_head

    if next_i >= N or next_j >= N: # 머리 이탈
        return
    if next_i < 0 or next_j < 0: # 머리 이탈
        return
    if next_head in tails: # 몸에 부딪힘
        return
    
    tails.append(head) # 현 위치를 몸통으로
    if next_head in apples: # 사과 있는 곳이면
        apples.remove(next_head) # 사과 제거
    else: # 사과 없으면
        tails.pop(0) # 첫번째 위치 제거

    if cnt == moves[k][0]:  # cnt == t 이면, 방향 바뀜
        current_dir = get_next_dir(current_dir, moves[k][1])
        if k + 1 < len(moves):
            k += 1
    
    move(next_head)

move((0,0))
print(cnt)
