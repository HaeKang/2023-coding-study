import sys

d_in = sys.stdin.readline
N,M = list(map(int, d_in().split()))
dat = list(int(d_in()) for _ in range(N))

mi = 1 # or min(dat)
ma = 1e9
res = 1

while ma >= mi:
    cnt = 1
    mid = int((ma + mi) / 2)
    left_money = mid
    break_trig = False
    for dm in dat:
        if left_money < dm:
            cnt += 1
            left_money = mid
        left_money -= dm

        if dm > mid or cnt > M:
            mi = mid + 1
            break_trig = True
            #print('breaker')
            break

    if not break_trig:
        res = mid
        ma = mid - 1

print(res)