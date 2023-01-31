N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
for A_i in A:
    cnt = 1 # 총감독관
    if A_i-B > 0: # 이걸 안해서 처음에 틀린...
        cnt += (A_i-B) // C
        cnt += int((A_i-B) % C > 0)
    total += cnt

print(total)