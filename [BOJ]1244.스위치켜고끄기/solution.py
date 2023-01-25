N = int(input())
switch = list(map(int,input().split()))
M = int(input())

def boy(num):
    global switch

    for i in range(N):
        if (i+1) % num == 0:
            switch[i] = int(not switch[i])

def girl(num):
    global switch
    idx = num-1
    k = 0
    while((idx-k >= 0 and idx+k < N) and # 안넘고, 상태가 같은 경우에만 계속 확장
          switch[idx-k] == switch[idx+k]):
        switch[idx-k] = int(not switch[idx-k])
        if k >= 1:
            switch[idx+k] = int(not switch[idx+k])
        k += 1

for i in range(M):
    g, num = map(int, input().split())

    if g == 1:
        boy(num)
    else:
        girl(num)

i = 0
while(i < N):
    s = []
    for j in range(i, i+20):
        if j >= N:
            break
        s.append(str(switch[j]))
    print(' '.join(s))
    i += 20