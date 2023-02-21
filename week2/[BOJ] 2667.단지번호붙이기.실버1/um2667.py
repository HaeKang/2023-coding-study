import sys
import queue

class danzi():
    def __init__(self,N,dat):
        self.N = N
        self.dat = dat
        self.ck = [[False for _ in range(self.N)] for __ in range(self.N)]
        #print("ck : ", self.ck)
        self.define_move()
        self.outs = list()
        self.q = queue.Queue()

    def define_move(self):
        self.dx = [1,0,-1,0]
        self.dy = [0,1,0,-1]

    def run(self):
        for kka in range(self.N):
            for kki in range(self.N):
                self.searcher(kki,kka)
        print(len(self.outs))
        self.outs.sort()
        for kka in range(len(self.outs)):
            print(self.outs[kka])

    def searcher(self,x,y):
        if not self.ck[y][x]:
            self.ck[y][x] = True
            if self.dat[y][x] == 1:
                cnt = 1
                self.bfs(x,y)
                while(not self.q.empty()):
                    nx,ny = self.q.get()
                    self.bfs(nx,ny)
                    cnt += 1

                self.outs.append(cnt)

    # bfs 만 쓰려는데 dfs 를 손가락이 쓰려함.
    def bfs(self,x,y):
        for kka in range(4):
            ny = y + self.dy[kka]
            nx = x + self.dx[kka]
            if (0 <= ny < self.N) and (0 <= nx < self.N):
                if (self.dat[ny][nx] == 1) and (self.ck[ny][nx] == False):
                    self.q.put([nx,ny])
                self.ck[ny][nx] = True
                #cnt += 1

'''
#in_data = sys.stdin.readline()
N = sys.stdin.readline()
#N = map(int, in_data)
print("sgsdgsd ", N)
#dat = [map(lambda x: int(in_data[i]), in_data) for _ in range(N)]
#dat = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
dat = [list(sys.stdin.readline().split("/n")) for _ in range(N)]

print(N)
print(dat)
print("end")
#'''

#'''
## Get data
N = int(input())

# 행렬 만들기
dat = [list(map(int, input())) for _ in range(N)]
#print(dat)
dz = danzi(N,dat)
dz.run()
#print("end")
#'''
