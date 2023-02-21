import sys

class jusa():
    def __init__(self,all_dat):
        self.n,self.m,self.x,self.y,self.myung,self.dat,self.order = all_dat
        # 움직이는 방향을 동 남 서 북 방향으로 고쳐주었습니다.
        for kka in range(self.myung):
            if self.order[kka] == 1:
                self.order[kka] = 0
            elif self.order[kka] == 4:
                self.order[kka] = 1

        self.dx = [1,0,-1,0]
        self.dy = [0,1,0,-1]

        # 주사위는 4x3 행렬로 나타내었습니다.
        self.cube = [[0 for kka in range(3)] for kki in range(4)]

    def out_check_move(self,kka):
        nx = self.x + self.dx[self.order[kka]]
        ny = self.y + self.dy[self.order[kka]]
        if 0 <= nx < self.m and 0 <= ny < self.n :
            self.x = nx
            self.y = ny
            return True

        else :
            return False

    # 좌우(동서) 방향으로 움직이는 경우와 상하(북남) 으로 움직은 경우로 나누었습니
    # 좌우 일때 1번째 행에 좌 혹은 우에 상판을 붙여주고 겹치는부분 잘라내어 self.cube에
    # 입력되었습니다. 상하도 로직은 동일합니다.

    def cube_update(self,kka):
        nc = list()
        for kki in range(4):
            nc.append(self.cube[kki][:])

        if self.order[kka] == 0 or self.order[kka] == 2:
            if self.order[kka] == 0:
                tl = nc[1] + [nc[3][1]]
                self.cube[3][1] = tl[0]
                del tl[0]
            else :
                tl = [nc[3][1]] + nc[1]
                self.cube[3][1] = tl[-1]
                del tl[-1]

            self.cube[1] = tl[:]

        else:
            tl = list()
            for kki in range(4):
                tl.append(nc[kki][1])
            if self.order[kka] == 1:
                tl = tl + [tl[0]]
                del tl[0]
            else :
                tl = [tl[-1]] + tl
                del tl[-1]
            for kki in range(4):
                self.cube[kki][1] = tl[kki]
        #print()
        #for kku in range(4):
        #    print(self.cube[kku])
    def num_printer(self,kka):
        self.cube_update(kka)
        if self.dat[self.y][self.x] == 0:
            self.dat[self.y][self.x] = self.cube[1][1]
        elif self.dat[self.y][self.x] > 0:
            self.cube[1][1] = self.dat[self.y][self.x]
            self.dat[self.y][self.x] = 0

        #for kku in range(self.n):
        #    print(self.dat[kku])
        print(self.cube[3][1])

    # 문제에 x,y 가 헤깔리게 나와있네요
    # 
    # out check move
    # 움직일 위치가 움직이기 가능한 위치인지 확인하고 가능한 곳이면 큐브의 위치를 업데이트 합니다
    # 
    # num printer
    # 주사위 위치를 업데이트 하는 cube update 후 바닥 조건에 따라 업데이트 해줍니다.
    def run(self):
        for kka in range(self.myung):
            if self.out_check_move(kka):
                self.num_printer(kka)

n,m,x,y,myung = list(map(int, sys.stdin.readline().split()))
dat = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
order = list(map(int, sys.stdin.readline().split()))
"""
print(n, ' ', m, ' ', x, ' ', y, ' ', myung, ' ' )
print( dat)
print(order)
"""
#js = jusa([n,m,x,y,myung,dat,order])
js = jusa([n,m,y,x,myung,dat,order]) # 
js.run()






