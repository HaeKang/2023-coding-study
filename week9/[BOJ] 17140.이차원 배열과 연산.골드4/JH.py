import sys
from collections import Counter
from itertools import chain

r,c,k = map(int, input().split())

A = []
for i in range(3):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

def R():
    global A

    renew = [] # 새로 만들어줄 A
    max_len = 0
    for i in range(len(A)):
        new_list = []
        row = A[i] # 현재 배열의 가로 (row)
        cnt = Counter(row) # {1 : 1의 개수, 2: 2의 개수 ...}
        for k, v in cnt.items():
            if k == 0: continue # 0은 무시
            new_list.append([k,v]) # 숫자, 횟수로 새로운 리스트에 담고
        new_list = sorted(new_list, key=lambda x : (x[1], x[0])) # 새로운 리스트를 개수로 sort
        new_list = list(chain.from_iterable(new_list)) # [[3, 1], [2, 3]] --> [3, 1, 2, 3]
        if len(new_list) > 100: # 100 이상이면 100까지만
            new_list = new_list[:100]
        renew.append(new_list) # A에 담기
        max_len = max(max_len, len(new_list)) # 길이 세주기
        
    for i in range(len(renew)):
        if len(renew[i]) < max_len:
            renew[i] = renew[i] + [0] * (max_len - len(renew[i])) # 모자라는 길이는 0으로 채우기
    A = renew

def C():
    global A

    def rotate(): # 배열의 가로/세로 바꾸기
        global A
        rotated = []
        for j in range(len(A[0])):
            new_arr = []
            for i in range(len(A)):
                new_arr.append(A[i][j])
            rotated.append(new_arr)
        A = rotated

    # 돌린다음 R연산 다시 돌리기
    rotate()
    R()
    rotate()


def test_print():
    n_row = len(A)
    for i in range(n_row):
        print(' '.join(list(map(str, A[i]))))
    print()

time = 0
while True:

    if r <= len(A) and c <= len(A[0]):
        if A[r - 1][c - 1] == k:
            break

    time += 1
    if time > 100: # 100초인데 안된 거면
        time = -1
        break

    n_row, n_col = len(A), len(A[0])
    if n_row >= n_col:
        R()
    else:
        C()

print(time)