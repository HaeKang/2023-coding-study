n = int(input())
arr = list(map(int, input().split()))

ans = arr[0]
tmp = arr[0]

for x in arr[1:]:
    if tmp < 0:   #연속합이 0보다 작으면 새로 시작
        tmp = x
    else:
        tmp += x

    ans = max(ans, tmp)
    
print(ans)