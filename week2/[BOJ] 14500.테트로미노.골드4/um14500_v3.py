import sys
import queue

class tet():
    def __init__(self,n,m,dat):
        self.n = n
        self.m = m
        self.dat = dat
        self.dx = [1,0,-1,0]
        self.dy = [0,1,0,-1]
        self.max = 0

    def run(self):
        n = self.n
        m = self.m

        for kka in range(n):
            for kki in range(m):
                self.checker(kki,kka)
        print(self.max)

    def updater(self,st,p1,p2):
        if 0 <= p1[0] < self.m and 0 <= p1[1] < self.n and 0 <= p2[0] < self.m and 0 <= p2[1] < self.n:
            val = st + self.dat[p1[1]][p1[0]] + self.dat[p2[1]][p2[0]]
            if val > self.max:
                self.max = val

    def six_check(self,p1,p2):
        sixd = list()
        for kka in range(4):
            temp_x = p1[0]+self.dx[kka]
            temp_y = p1[1]+self.dy[kka]
            if [temp_x,temp_y] != p2:
                sixd.append([temp_x,temp_y])
            temp_x = p2[0]+self.dx[kka]
            temp_y = p2[1]+self.dy[kka]
            if [temp_x,temp_y] != p1:
                sixd.append([temp_x,temp_y])
        if len(sixd) != 6:
            print('six check err')

        st = self.dat[p1[1]][p1[0]] + self.dat[p2[1]][p2[0]]
        for kka in range(6):
            for kki in range(5-kka):
                self.updater(st,sixd[kka],sixd[-kki-1])

    def edge_check_x(self,x,y):
        st = self.dat[y][x] + self.dat[y][x+1]
        self.updater(st,[x-1,y],[x-1,y+1])
        self.updater(st,[x,y+1],[x-1,y+1])

        self.updater(st,[x+2,y+1],[x+1,y+1])
        self.updater(st,[x+2,y+1],[x+2,y])

        self.updater(st,[x+2,y-1],[x+2,y])
        self.updater(st,[x+2,y-1],[x+1,y-1])

        self.updater(st,[x-1,y-1],[x-1,y])
        self.updater(st,[x-1,y-1],[x,y-1])

    def edge_check_y(self, x, y):

        st = self.dat[y][x] + self.dat[y+1][x]
        self.updater(st,[x-1,y+2],[x-1,y+1])
        self.updater(st,[x-1,y+2],[x,y+2])

        self.updater(st,[x+1,y+2],[x,y+2])
        self.updater(st,[x+1,y+2],[x+1,y+1])

        self.updater(st,[x+1,y-1],[x+1,y])
        self.updater(st,[x+1,y-1],[x,y-1])

        self.updater(st, [x - 1, y - 1], [x - 1, y])
        self.updater(st, [x - 1, y - 1], [x, y - 1])

    # 기준이 되는 좌표는 가로 세로 두개의 셀로 잡음.

    # six_check 함수
    # 인접한 두개의 셀의 면에 해당하는 좌표(6개) 중 두개를 골라 현재 최대감(self.max) 과 비교

    # edge check 함수
    # 인접한 두개의 셀의 엣지(4개)와 연결될 수있는 8가지 케이스 각각을 현재 최대값과 비교
    #
    # 첫 파일 um14500 모든 케이스를 이중 포문 안에서 겹치는 경우를 최소화 하려다 실패
    # v2 파일 각행과 각 열 마지막 인덱스는 이전 인덱스의 과정에서 포함된 경우로 착각. 각 마지막 인덱스에 해당하는 부문만 포함시킴. 84 % 에서 틀림
    #
    def checker(self,x,y):
        if y + 1 < self.n:
            self.six_check([x,y],[x,y+1])
            self.edge_check_y(x,y)
        if x + 1 < self.m:
            self.six_check([x+1,y],[x,y])
            self.edge_check_x(x,y)




n,m = list(map(int, sys.stdin.readline().split()))
dat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
tt = tet(n,m,dat)
#print(n,'  ',m)
#print(dat)
tt.run()