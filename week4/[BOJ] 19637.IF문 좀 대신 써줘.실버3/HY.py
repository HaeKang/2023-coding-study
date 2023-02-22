import sys
input = sys.stdin.readline
 
#이분탐색
def solution(x):
    start, end = 0, len(power_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if x > power_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    print(name_list[end + 1])
    
n, m = map(int, input().split())
name_list = []
power_list = []
for _ in range(n):
    name, power = input().split()
    if power_list and power_list[-1] == int(power):  #중복되는 값은 무시하기
        continue
    name_list.append(name)
    power_list.append(int(power))
    
for _ in range(m):
    p = int(input())
    solution(p)