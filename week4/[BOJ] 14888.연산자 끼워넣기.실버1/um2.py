import sys
import copy
'''
operation 수를 그대로 받아서 사용
for 문 사용시 전체 operation 을 하나씩 찾는 bfs 대신
연산별 로 최대 4개(+ - * /) 중 남아있는 연산을 실행하는 Bfs 사용:ㅈㅂ
챗gpt 한테 물어보니 
for 문 대신 각 연산에 대해 스택을 이용하면 더 빠르다고 하네요(3배 빠름)
if op[0] > 0:
        op[0] -= 1
        dfs(n+1, res + dat[n+1])
        op[0] += 1
이런식으로...
'''
d_in = sys.stdin.readline
N = int(d_in())
dat = list(map(int, d_in().split()))
op = list(map(int, d_in().split()))
r_max = -1e9
r_min = 1e9

def bfs(n,op,val):
    global N,dat
    if n == N-1:
        global r_min, r_max
        r_max = max(r_max, val)
        r_min = min(r_min, val)
        return

    for kka in range(4):
        if op[kka] != 0:
            op_t = copy.deepcopy(op)
            op_t[kka] -= 1
            if kka == 0:
                nval = val + dat[n+1]
            elif kka == 1:
                nval = val - dat[n+1]
            elif kka == 2:
                nval = val * dat[n+1]
            else:
                nval = val / dat[n+1]
            bfs(n+1,op_t,int(nval))

bfs(0,op,dat[0])
print(r_max)
print(r_min)
