N = int(input())
arr = list(map(int, input().split()))
dp_arr = [0] * N

dp_arr[0] = arr[0]

for i in range(1,N):
    dp_arr[i] = max(dp_arr[i-1] + arr[i], arr[i]) # i-1 번째 부분합 + arr[i] 와 arr[i] 비교하여 새로 연속을 시작할 지 보기 (좀 비직관적임..)

print(max(dp_arr))