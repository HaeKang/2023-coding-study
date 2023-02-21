## 실패 ## 

import copy

N = int(input())

board = []
for i in range(N):
    board.append(list(map(int, input().split())))

largest = 2

# 상 하 좌 우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def move(dir):
    global board

    if dir == 0:
        for i in range(N):
            for j in range(N):
                if board[j][i] > 0:
                    k = 1
                    while (j - k >= 0 and board[j-k][i] == 0):
                        k += 1
                    k -= 1
                    temp = board[j-k][i]
                    board[j-k][i] = board[j][i]
                    board[j][i] = temp

    if dir == 1:
        for i in range(N):
            for j in range(N):
                if board[j][i] > 0:
                    k = 1
                    while (j + k < N and board[j+k][i] == 0):
                        k += 1
                    k -= 1
                    temp = board[j+k][i]
                    board[j+k][i] = board[j][i]
                    board[j][i] = temp

    if dir == 2:
        for i in range(N):
            for j in range(N):
                if board[i][j] > 0:
                    k = 1
                    while (j - k >= 0 and board[i][j - k] == 0):
                        k += 1
                    k -= 1
                    temp = board[i][j - k]
                    board[i][j - k] = board[i][j]
                    board[i][j] = temp

    if dir == 3:
        for i in range(N):
            for j in range(N-1, -1, -1):
                if board[i][j] > 0:
                    k = 1
                    while (j + k < N and board[i][j + k] == 0):
                        k += 1
                    k -= 1
                    temp = board[i][j + k]
                    board[i][j + k] = board[i][j]
                    board[i][j] = temp


def merge(dir):
    global board

    if dir == 0:
        for i in range(N):
            j = 0
            while(j+1 < N):
                if board[j][i] == board[j+1][i]:
                    board[j][i] *= 2
                    board[j+1][i] = 0
                    j += 2
                else:
                    j += 1

    if dir == 1:
        for i in range(N):
            j = N-1
            while(j-1 >= 0):
                if board[j][i] == board[j-1][i]:
                    board[j][i] *= 2
                    board[j-1][i] = 0
                    j -= 2
                else:
                    j -= 1

    if dir == 2:
        for i in range(N):
            j = 0
            while(j+1 < N):
                if board[i][j] == board[i][j+1]:
                    board[i][j] *= 2
                    board[i][j+1] = 0
                    j += 2
                else:
                    j += 1

    if dir == 3:
        for i in range(N):
            j = N-1
            while(j-1 >= 0):
                if board[i][j] == board[i][j-1]:
                    board[i][j] *= 2
                    board[i][j-1] = 0
                    j -= 2
                else:
                    j -= 1

def test_print():
    for i in range(N):
        str_list = []
        for j in range(N):
            str_list.append(str(board[i][j]))
        print(' '.join(str_list))
    print()

def operation(movings): # 방향 정해지면 그에 따라 moving - merging - moving
    global board, largest
    initial_board = copy.deepcopy(board)

    for dir in movings:
        move(dir)
        merge(dir)
        move(dir)

    for i in range(N):
        for j in range(N):
            largest = max(largest, board[i][j])

    board = initial_board # 다시 원상복귀


selected = []
def select():
    global selected

    if len(selected) == 5:
        operation(selected)
        return

    for k in range(4):
        selected.append(k)
        select()
        selected.pop()

select()
print(largest)
