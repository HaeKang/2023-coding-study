import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))


start = min(arr)
end = sum(arr)

while start <= end:
    mid = (start + end) // 2  # k원

    money = mid
    cnt = 1  # 인출횟수

    if mid < max(arr):
        start = mid + 1
        continue

    for i in range(n):
        if money < arr[i]:
            money = mid - arr[i]
            cnt += 1

            if cnt > m:
                break
        else:
            money -= arr[i]

    # 출금금액 ++
    if cnt > m:
        start = mid + 1
    # 출금금액 --
    else:
        end = mid - 1
        k = mid

print(k)
