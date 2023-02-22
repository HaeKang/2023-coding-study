import sys
N,M,H = map(int, input().split())

original_bridge = []
for i in range(M):
    y,x = map(int, sys.stdin.readline().rstrip().split())
    original_bridge.append((y-1,x-1))


area = []
def check(total_bridge): # 갈 수 있는지 체크
    global area

    area = [] # 맵을 만들어서
    for i in range(H):
        area.append([0] * N)

    for by, bx in total_bridge: # 사다리를 놓고
        area[by][bx] = 1

    for j in range(N): # 내려가보기
        k = j
        for i in range(H):
            if area[i][k] == 1: # 항상 왼쪽만 사다리가 놓아짐
                k += 1
            elif k-1 >= 0 and area[i][k-1] == 1:
                k -= 1

        if not k == j:
            return False

    return True

ret = -1
picked = []

idx_area = []
l = 0
for i in range(H):
    row = []
    for j in range(N):
        row.append(l)
        l += 1
    idx_area.append(row)


def select_bridge(k):
    global ret

    if len(picked) == k:
        if check(picked + original_bridge):
            ret = k # 되면 k
        return

    for i in range(H):
        for j in range(N-1):
            pos0 = (i, j-1)
            pos1 = (i, j)
            pos2 = (i, j+1)

            if pos0 in picked or pos0 in original_bridge:
                continue

            if pos1 in picked or pos2 in picked:
                continue
            if pos1 in original_bridge or pos2 in original_bridge:
                continue

            if len(picked) < 1 or idx_area[picked[-1][0]][picked[-1][1]] < idx_area[pos1[0]][pos1[1]]: # 백트래킹
                picked.append(pos1)
                select_bridge(k)
                picked.pop()


for i in range(4):
    select_bridge(i)
    if ret >= 0:
        break
print(ret)