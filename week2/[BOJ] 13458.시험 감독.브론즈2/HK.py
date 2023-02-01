n = int(input())
arr = map(int, input().split())
b, c = map(int, input().split())

arr = sorted(arr, reverse=True)

ans = 0

for i in range(0, n):
    if arr[i] != 0:
        ans += 1
        arr[i] -= b  # 총감독관

        if arr[i] > 0:
            ans += arr[i] // c
            if arr[i] % c != 0:
                ans += 1

print(ans)
