n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

start, end = 0, trees[-1]
ans = 0

#이분탐색
while start <= end:
    total = 0
    mid = (start + end) // 2
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total < m:     #나무가 길이가 적으면 mid 값 감소
        end = mid - 1
    else:
        ans = mid
        start = mid + 1
        
print(ans)