import sys

N = int(sys.stdin.readline().split()[0])
inwon = list(map(int, sys.stdin.readline().split()))
B,C = list(map(int, sys.stdin.readline().split()))

#print(N)
#print(inwon)
#print(B,' ',C)

tot_gam = 0
# 입력 조건에 응시가의 수가 양수여서 for 문 다음줄 조건을 없이 했더니 틀렸네요.
# 이런 경우도 있나요..?
for kka in range(N):
    if inwon[kka] > 0:
        tot_gam += 1
        val = inwon[kka] - B
        if val > 0 :
            val2 = int(val/C)
            tot_gam += val2
            #if val/C - val2 > 0:
            if val % C != 0:
                tot_gam += 1

print(tot_gam)