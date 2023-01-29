n = int(input())
arr = list(map(int, input().split()))
b, c = map(int, input().split())

#총 감독관 1명씩
ans = len(arr)

for i in arr:
    if i - b > 0:
        if (i - b) % c != 0:
            ans += (i - b) // c + 1
        else:
            ans += (i - b) // c

print(ans)