import sys
from collections import deque
# 2시간 20분
in_d = sys.stdin.readline
R, C, T = list(map(int, in_d().split()))
mat = [list(map(int, in_d().split())) for _ in range(R)] # 먼지 퍼지기 전 상태
hmat = [[list() for c in range(C)] for _ in range(R)] # 퍼진 먼지만 저장
dy = [0,1,0,-1]
dx = [1,0,-1,0]
ur, uc, dr, dc = 0,0,0,0 # 기계위치

def gcp():
    global ur,uc,dr,dc,R,C,mat
    for r in range(R):
        for c in range(C):
            if mat[r][c] == -1:
                ur, uc, dr, dc = r, c, r+1, c
                return
gcp()
def hwaksan(): # 확산
    global mat, hmat, R, C, idx
    mat_temp = [[list() for c in range(C)] for _ in range(R)] # 확산 먼지 초기화
    # 확산 된 먼지는 4방향에서 각각 올 수 있으므로 리스트에다 추가함!
    for r in range(R):
        for c in range(C):
            if mat[r][c] > 0 or sum(hmat[r][c]) > 0: # 먼지 존재 확인 / 위치에 전 타임스텝의 먼지가 있고 확산된 먼지가 있는지 확인
                mat[r][c] += sum(hmat[r][c]) # 해당위치에 먼지 += 해당위치로 퍼진 먼지
                val = int(mat[r][c] / 5) # 1/5
                for i in range(4): # 방향마다
                    nr, nc = r + dy[i], c + dx[i]
                    if (not (0 <= nr < R and 0 <= nc < C)) or mat[nr][nc] == -1:
                        continue
                    mat_temp[nr][nc].append(val) # 퍼트림을 리스트에 집어넣음
                    mat[r][c] -= val # 퍼트렸으면 원래 먼지 빼주고
    hmat = mat_temp # 확산 먼지 업데이트
    return

def gonggi():
    global ur,uc,dr,dc,R,C,mat,hmat
    # up
    '''
    ls, rs = list(), list()
    for r in range(1,ur-1):
        mat[r][0] += sum(hmat[r][0])
        mat[r][-1] += sum(hmat[r][-1])
        ls.append(mat[r][0])
        rs.append(mat[r][-1])
    Q_ls, Q_rs, Q_up, Q_dw = deque(ls), deque(rs), deque(mat[0]), deque(mat[ur])
    Q_ls.appendleft(Q_up.popleft())
    Q_dw.appendleft(Q_ls.pop())
    Q_rs.append(Q_dw.pop())
    Q_up.append(Q_rs.popleft())
    '''
    # 위아래 따로 돌림
    # up
    mat[ur] = [-1] + mat[ur]
    hmat[ur] = [[0]] + hmat[ur]
    mat[0] = mat[0] + [mat[1][-1]]
    hmat[0] = hmat[0] + [hmat[1][-1]]
    mat[ur][1], hmat[ur][1] = 0, [0]
    for r in range(1,ur):
        mat[ur-r][0] = mat[ur-r-1][0]
        hmat[ur-r][0] = hmat[ur-r-1][0]
        mat[r][-1] = mat[r+1][-1]
        hmat[r][-1] = hmat[r+1][-1]
    del mat[ur][-1], hmat[ur][-1], mat[0][0], hmat[0][0]
    # down
    mat[dr] = [-1] + mat[dr]
    hmat[dr] = [[0]] + hmat[dr]
    mat[-1] = mat[-1] + [mat[-2][-1]]
    hmat[-1] = hmat[-1] + [hmat[-2][-1]]
    mat[dr][1], hmat[dr][1] = 0,[0]
    for r in range(dr+1,R-1):
        mat[R-(r-dr)-1][-1] = mat[R-(r-dr)-2][-1]
        hmat[R-(r-dr)-1][-1] = hmat[R-(r-dr)-2][-1]
        mat[r][0] = mat[r+1][0]
        hmat[r][0] = hmat[r+1][0]

    del mat[dr][-1], hmat[dr][-1], mat[-1][0], hmat[-1][0]
    return




for _ in range(T):
    hwaksan()
    #print('----------')
    #mat[0][0] = 55
    #mat[dr][-1] = 222
    #mat[dr+1][-1] = 2222
    #mat[-1][0] = 88
    #for kka in range(R):
    #    print(mat[kka])
    gonggi()
    #print('----------')
    #for kka in range(R):
    #    print(mat[kka])
#print('----------')
#for kka in range(R):
#    print(hmat[kka])
#print('----------')
#for kka in range(R):
#    print(mat[kka])
#print('----------')
misae = 2
for r in range(R):
    misae += sum(mat[r]) + sum([sum(hmat[r][c]) for c in range(C)])
#print('----------')
print(misae)