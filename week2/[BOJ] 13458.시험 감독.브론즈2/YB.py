n = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())
answer = 0

for num in arr:
    check = False
    while num > 0:
        if not check:
            num -= B
            answer += 1
            check = True
        else:
            if num%C == 0:
                answer += num//C
            else:
                answer += (num//C+1)
            num = 0
print(answer)
