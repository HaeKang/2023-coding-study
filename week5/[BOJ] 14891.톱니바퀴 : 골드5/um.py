import sys

in_d = sys.stdin.readline
tobni = [list(in_d().split('\n')[0]) for _ in range(4)] # 12 start
# 2 right -1 left %
K = int(in_d())
ord = [list(map(int,in_d().split())) for _ in range(K)]

def checker():
    global tobni
    res = list()
    for kka in range(3):
        if tobni[kka][2] != tobni[kka+1][-2]:
            res.append(True)
        else:
            res.append(False)
    return res

def _turn(n,dir):
    global tobni
    if dir == 1:
        tmp = tobni[n][-1]
        del tobni[n][-1]
        tobni[n] = [tmp] + tobni[n]
    else:
        tmp = tobni[n][0]
        del tobni[n][0]
        tobni[n] = tobni[n] + [tmp]


def turn(ord_n):
    #print("++++")
    global ord
    m_tob = checker() # 어디를 돌려야하는지 체크
    #print(m_tob)
    od = ord[ord_n]
    trig = True # 이전 톱니 돌아갔는지 체크
    td = od[1]
    _turn(od[0]-1,od[1]) # 기준 돌리기
    for kka in range(od[0],4): # 기준 오른쪽으로 돌리기
        if m_tob[kka-1] and trig:
            _turn(kka, -td)
            td *= -1 # 톱니 방향 전환
        else :
            trig = False
    trig = True
    td = od[1]
    for kka in range(od[0],1,-1): # 기준 왼족으로 돌리기
        if m_tob[kka-2] and trig:
            _turn(kka-2, -td)
            td *= -1
        else:
            trig = False

    #for kka in range(4):
    #    print(tobni[kka])

for kka in range(K):
    turn(kka)
    #sdg

re = 0
for kka in range(4):
    #print('sgs',pow(2,kka))
    re += pow(2,kka) * int(tobni[kka][0])
    #print(tobni[kka])

#print('re')
print(re)