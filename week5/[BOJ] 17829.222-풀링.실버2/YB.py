n = int(input())
def pooling(arr):
    n, m = len(arr), len(arr[0])
    new = [[-10001]*(m//2) for _ in range(n//2)]
    for i in range(n//2):
        for j in range(m//2):
            temp = arr[i*2:i*2+2]
            check = []
            check.extend(temp[0][j*2:j*2+2])
            check.extend(temp[1][j * 2:j * 2 + 2])
            check.sort()

            new[i][j] = check[-2]
    return new

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

while True:
    if len(arr) == 1:
        print(arr[0][0])
        break
    arr = pooling(arr)
