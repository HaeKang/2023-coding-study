import sys
# ⌊(합쳐진 파이어볼 질량의 합)/5⌋ 나머지 버린다는 의미
# 순환
in_d = sys.stdin.readline
N, M, K = list(map(int, in_d().split()))
fb = [list(map(int, in_d().split())) for _ in range(M)]
#for kka in range(M):
#    ㅇ
dx = [0,1,1,1,0,-1,-1,-1] # 방향
dy = [-1,-1,0,1,1,1,0,-1]
for __ in range(K):
    mat_dict = dict()
    for bn in range(len(fb)):
        y,x,m,s,d = fb[bn]
        ny, nx = y + s * dy[d], x + s * dx[d]
        ny = (ny - 1) % N + 1 # 순환
        nx = (nx - 1) % N + 1
        nn = str(ny) + '_' + str(nx)
        if nn in mat_dict: # dict 에 y_x 를 key 값으로 msd 추가 ( 기존에 yx 같은 좌표에 fb가 있을경우)
            mat_dict[nn].append([m,s,d])
        else: # 기존에 yx 같은 좌표에 fb 가 없을 경우
            mat_dict[nn] = list()
            mat_dict[nn].append([m,s,d])
    #print(mat_dict)
    fb = list()
    for key,val in mat_dict.items(): # fb 가 있는 좌표만 불러옴 val 에는 각 fb 의 msd 가 있음
        y, x = list(map(int, key.split('_'))) # 좌표계 변환
        if len(val) == 1: # fb 가 하나만 있으면 쪼개지지 않음
            fb.append([y,x,val[0][0],val[0][1],val[0][2]])
            continue
        m, s, hol, zzak = 0, 0, False, False # 새로운 ms 정의 / 방향이 전부 홀인지 짝인지 체크위한 변후
        for kka in range(len(val)):
            if kka == 0: # 루프 시작에 짝이나 홀이면 해당 트리거 온
                if val[kka][-1] % 2 == 0:
                    zzak = True
                else :
                    hol = True
            else: # 루프 처음 시작이후 홀이나 짝이 유지되지 않으면 트리거 오프
                if zzak and val[kka][-1] % 2 != 0:
                    zzak = False
                if hol and val[kka][-1] % 2 != 1:
                    hol = False
            m += val[kka][0]
            s += val[kka][1]

        nm = int(m/5)
        if nm == 0: # 질량 0 되면 fb 사라짐
            continue
        ns = int(s/len(val)) # 속도 갱신
        nd = False
        if zzak or hol: # 홀짝 트리거 살아있는 경우 상하좌우
            nd = [0,2,4,6]
        else: # 홀짝 트리거 오프 인경우 대각선
            nd = [1,3,5,7]
        for kka in range(4): # 4방향에 대해 새로운 fb 넣어줌
            fb.append([y,x,nm,ns,nd[kka]])

res_m = 0
for kka in range(len(fb)):
    res_m += fb[kka][2]
print(res_m)