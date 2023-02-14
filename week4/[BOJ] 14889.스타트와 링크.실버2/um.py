import copy
import sys

# 순서없이 N/2 개 뽑기
in_d = sys.stdin.readline
N = int(in_d())
mat = [list(map(int,in_d().split())) for _ in range(N)]
res = 1e12

def cal_diff(chk,bo):
    global res,N,mat
    val = 0
    idx = list()
    for kka in range(N):
        if chk[kka] == bo:
            idx.append(kka)
    '''
    for n in range(int(N/2)):
        for kka in range(n+1,int(N/2)):
            val += mat[idx[n]][idx[kka]] + mat[idx[kka]][idx[n]]
    '''
    val = sum(mat[i][j] for i in idx for j in idx)
    return val

def bt(num,chk,st_idx):
    global res,N
    #if res == 0:
    #    return
    if num == 0:
        t1 = cal_diff(chk,True)
        t2 = cal_diff(chk,False)
        res = min(abs(t1-t2), res)
    for kka in range(st_idx,N):
        if chk[kka] == False:
            chk_t = copy.deepcopy(chk)
            chk_t[kka] = True
            bt(num-1,chk_t,kka+1)
    # 연산자 끼워넣기 처럼 첫팀에 넣고 bt 호출후 첫팀에서 제외 방식이 더 효율적
    # 즉 순서대로 각팀에 배치해보기

chk = [False for _ in range(N)]
chk[0] = True # 첫번째 애는 한팀으로 고정 // 다음 애부터 팀 나누면됨.
bt(int(N/2)-1,chk,1)
#print(res)
print(res)



