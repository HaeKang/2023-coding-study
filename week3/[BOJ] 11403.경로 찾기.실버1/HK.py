n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

# 거쳐가는 노드
for k in range(n):
    # 시작
    for i in range(n):
        # 종료
        for j in range(n):
            if arr[i][k] == 1 and arr[k][j] == 1:
                arr[i][j] = 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()
