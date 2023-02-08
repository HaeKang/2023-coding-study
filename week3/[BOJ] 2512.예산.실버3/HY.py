import sys
#input = sys.stdin.readline
n = int(input())
array = list(map(int, input().split()))
m = int(input())
start = 0
end = max(array)
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in array:
        if i <= mid:
            cnt += i
        else:
            cnt += mid
    if cnt <= m:
        start = mid + 1
    else: 
        end = mid - 1
        
print(end)