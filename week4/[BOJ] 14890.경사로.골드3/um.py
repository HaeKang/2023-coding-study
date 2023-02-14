import sys

d_in = sys.stdin.readline
N,L = list(map(int,d_in().split()))
mat = [list(map(int,d_in().split())) for _ in range(N)]
cnt = 0


def cal(dat):
    global N,L
    val = dat[0]
    c = 0
    g_trig = [False for _ in range(N)]
    for kka in range(1,N):
        if val == dat[kka]:
            continue
        if abs(val-dat[kka]) >= 2:
            return 0
        elif val-dat[kka] == 1: # 현재 칸이 한칸 낮아졌을 경우 이후 L 개의 경사로 배치(g_trig)
            if g_trig[kka]:
                return 0
            for l in range(L):
                if kka+l >= N:
                    return 0
                g_trig[kka+l] = True
        elif dat[kka]-val == 1: # 현채 칸이 한칸 높아졌을 경우 이전 L개의 경사로(g_trig)가 있는지 확인
            val_b = dat[kka-1]
            for l in range(L):
                if g_trig[kka-l-1] or kka-l-1 < 0 or val_b != dat[kka-l-1]: # 3번째; 높이가 달라졋을 경우 추가
                    return 0
                val_b = dat[kka-l-1]
        val = dat[kka]
    return 1

for kka in range(N):
    dx = mat[kka]
    dy = list()
    for kki in range(N):
        dy.append(mat[kki][kka])
    cnt += cal(dx)
    cnt += cal(dy)
print(cnt)

