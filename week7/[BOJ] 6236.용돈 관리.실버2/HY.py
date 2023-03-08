n, m = map(int, input().split())
case = []
for _ in range(n):
    case.append(int(input()))
#이분 탐색    
left = min(case)
right = max(case)

while left <= right:
    mid = (left + right) // 2
    money = mid
    cnt = 1
    for i in case:
        if money < i:
            money = mid
            cnt += 1
        money -= i
    
    if cnt > m or mid < max(case):
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
        
print(ans)        