import copy
import sys

N,M = map(int, input().split())

area = []
for i in range(N):
    area.append(list(map(int,sys.stdin.readline().rstrip().split())))

home = []
chick = []
selected = []

for i in range(N):
    for j in range(N):
        if area[i][j] == 1:
            home.append((i,j))
        elif area[i][j] == 2:
            chick.append((i,j))

def calculate_neighbor(home, selected):
    # O(N*M)
    def cal_dist(pos1, pos2): # pos = (y, x) tuple의 거리 계산
        return abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])

    min_total_dist = 0
    for pos1 in home:
        min_dist = 1E+10
        for pos2 in selected:
            min_dist = min(min_dist, cal_dist(pos1, pos2))
        min_total_dist += min_dist

    return min_total_dist

ret = 1E+10
def select():
    global selected, ret

    if len(selected) == M: # M개를 뽑았으면
        ret = min(ret, calculate_neighbor(home, selected)) # 가장 가까운 치킨집의 거리를 합하여 도시 치킨 거리를 구한다.
        return

    for i, pos in enumerate(chick):
        if len(selected) == 0 or chick.index(selected[-1]) < i: # M개의 치킨집을 뽑는데, 항상 마지막으로 선택한 치킨집의 index보다 큰 치킨 집을 뽑는다. (중복 제거, 조합)
            selected.append(pos)
            select()
            selected.pop()

select()
print(ret)