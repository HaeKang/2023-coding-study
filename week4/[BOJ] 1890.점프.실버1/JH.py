N = int(input())

area = []
for i in range(N):
    area.append(list(map(int, input().split())))

dp_arr = []
for i in range(N):
    dp_arr.append([0]*N)

def test_print():
    for i in range(N):
        print(' '.join(list(map(str, dp_arr[i]))))
    print()

dp_arr[0][0] = 1
for i in range(N):
    for j in range(N):

        if i == N-1 and j == N-1:
            break

        jump = area[i][j]

        if i + jump < N:
            dp_arr[i+jump][j] = dp_arr[i][j] + dp_arr[i+jump][j] # dp를 쓴다
        if j + jump < N:
            dp_arr[i][j+jump] = dp_arr[i][j] + dp_arr[i][j+jump]

#test_print()
print(dp_arr[N-1][N-1])