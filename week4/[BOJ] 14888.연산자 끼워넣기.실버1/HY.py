#완전탐색
import sys
from itertools import permutations
#input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

op_list = []
for _ in range(op[0]):
    op_list.append('+')
for _ in range(op[1]):
    op_list.append('-')
for _ in range(op[2]):
    op_list.append('*')
for _ in range(op[3]):
    op_list.append('%')
    
max = -1e9
min = 1e9
#연산자들 리스트에서 순열로 모든 조합 검사
for case in permutations(op_list, n - 1):
    cnt = arr[0]
    for i in range(1, n):
        if case[i - 1] == '+':
            cnt += arr[i]
        elif case[i - 1] == '-':
            cnt -= arr[i]
        elif case[i - 1] == '*':
            cnt *= arr[i]
        else:
            cnt = int(cnt / arr[i])
            
    if cnt > max:
        max = cnt
    if cnt < min:
        min = cnt
        
print(max)
print(min)