T = int(input())

p_arr = [0,1,1,1,2,2] + [i*0 for i in range(101-6)]

def P(N):
    if p_arr[N]:
        return p_arr[N]

    p_arr[N] = P(N-1) + P(N-5) # 다이나믹 프로그래밍
    return p_arr[N]

ret = []
for i in range(T):
    N = int(input())
    ret.append(P(N))

for r in ret:
    print(r)