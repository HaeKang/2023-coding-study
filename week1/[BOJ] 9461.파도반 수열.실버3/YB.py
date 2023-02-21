T = int(input())
for _ in range(T):
    n = int(input())
    arr = [1, 1, 1, 2, 2]

    if n <= 5:
        print(arr[n-1])
    else:
        arr = arr + [0 for _ in range(n-5)]
        for i in range(5, n):
            arr[i] = arr[i-5]+arr[i-1]
        print(arr[-1])
