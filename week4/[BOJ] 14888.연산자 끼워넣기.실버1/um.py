import copy
import sys
'''
각 연산을 새로운 리스트(oper) 에 넣어둠 [+ + + - - - - * * /] 
bfs 사용하여 순서대로 넣어보며 찾음.

oper 의 0번째 값인 + 를 시작하여 값을 구하고
다음 값을 구할 때 겹치는 연산 + 를 이용하기 때문에 겹치는 부분이 생김.
겹치는 부분 없애기 위해 다시 짬
'''
in_d = sys.stdin.readline
N = int(in_d())
dat = list(map(int,in_d().split()))
oper_d = list(map(int,in_d().split()))
# + - x /
r_max = -1e9
r_min = 1e9
oper = list()
for kka in range(oper_d[0]):
    oper.append('+')
for kka in range(oper_d[1]):
    oper.append('-')
for kka in range(oper_d[2]):
    oper.append('*')
for kka in range(oper_d[3]):
    oper.append('/')

def bfs(chk, n, val):
    global dat, oper
    if n == N-1:
        global r_max,r_min
        r_max = max(r_max, val)
        r_min = min(r_min, val)
        return

    bo = ' '
    trig = False
    for kka in range(0,N-1):
        if not chk[kka]:
            chk_t = copy.deepcopy(chk)
            chk_t[kka] = True
            if oper[kka] == '+' and (oper[kka] != bo or trig):
                nval = val + dat[n+1]
            elif oper[kka] == '-' and (oper[kka] != bo or trig):
                nval = val - dat[n+1]
            elif oper[kka] == '*' and (oper[kka] != bo or trig):
                nval = val * dat[n+1]
            elif oper[kka] == '/' and (oper[kka] != bo or trig):
                nval = val / dat[n+1]
            else:
                trig = True
                if oper[kka] == '+':
                    nval = val + dat[n + 1]
                elif oper[kka] == '-':
                    nval = val - dat[n + 1]
                elif oper[kka] == '*':
                    nval = val * dat[n + 1]
                elif oper[kka] == '/':
                    nval = val / dat[n + 1]
            bfs(chk_t, n+1, int(nval))

chk = [False for kka in range(N-1)]
bfs(chk, 0, dat[0])
print(r_max)
print(r_min)


