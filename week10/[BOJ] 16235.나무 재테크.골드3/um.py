import sys
import time
# 봄여름가을겨울 다 따로 짰다가 한번에 처리 했고 메모리 재 할당 다 없앴는데도 시간초과....
# sort 때문인가요?..
# um.py vs um2.py 시간 비교
#  0.04 vs 0.98 예제 8번 시간 10000회
in_d = sys.stdin.readline
N, M, K = list(map(int, in_d().split()))
mat_i = [list(map(int, in_d().split())) for _ in range(N)]
mat = [[[5, mat_i[y][x], 0, 0] for x in range(N)] for y in range(N)] # NxN 에 [현재양분, 겨울에추가되는양분(input), 최근업데이트년도, 추가할양분]
namus = [list(map(int, in_d().split())) for _ in range(M)] # 나무 전체 리스트
dy = [0,1,1,1,0,-1,-1,-1]
dx = [1,1,0,-1,-1,-1,0,1]
t1 = time.time()
for _ in range(10000):
    for t in range(K):
        # spring
        namus.sort() # 나무스에 모든 나무 위치가 들어있고 마지막 인덱스는 나이이기 때문에 소팅
        dead_cnt = 0 # 죽은 나무 개수
        for i in range(len(namus)): # 나무가 있는 위치만 업데이트 할거임
            #(x, y, k) = namus[i] # r c 에서 y x 로 어떻게 마뀌는건지 안나와있음.
            (y, x, k) = namus[i-dead_cnt] # 나무의 위치와 나이
            if mat[y-1][x-1][2] != t: # 양분 업데이트 이번 해에 안했으면
                mat[y-1][x-1][0] += mat[y-1][x-1][3] # 이전에 죽은 애들 더해주고
                mat[y-1][x-1][3] = 0 # 죽은애들 값 초기화 해주고
                mat[y - 1][x - 1][0] += (t - mat[y - 1][x - 1][2]) * mat[y - 1][x - 1][1] # 양분 업데이트 안한 햇수 만큼 양분 더해주고
                mat[y-1][x-1][2] = t # 업데이트 시기 금년으로 바꿔주고

            if mat[y-1][x-1][0] >= k: # 나무 살 수 있으면
                mat[y-1][x-1][0] -= k
                namus[i-dead_cnt] = (y,x,k+1) # 해당 나무 나이 한살 올리고
                if (k+1) % 5 == 0: # 한살 올렸는데 5의 배수면 번식
                    for d in range(8):
                        ny, nx = y + dy[d], x + dx[d]
                        if not (0 < nx <= N and 0 < ny <= N):
                            continue
                        namus.append((ny, nx, 1)) # 뒤쪽에 추가
            else: # 나무 죽었으면
                mat[y-1][x-1][3] += int(k/2) # mat 마지막 인덱스에 다음 양분 업데이트할 때 더해줄 값 추가
                del namus[i-dead_cnt] # 나무 죽었으니 빼주고
                dead_cnt += 1 # 루프문 중간 리스트가 빠졌으니 보정해줄 죽은 나무 갯수 하나 더해줌
        # summer
        '''
        for i in range(len(d_namu)):
            #(x,y,k) = d_namu[i]
            (y,x,k) = d_namu[i]
            mat[y-1][x-1][0] += int(k/2)
        '''
        # fall
        '''
        for i in range(len(n_namu)):
            (y,x,k) = n_namu[i]
            if k % 5 == 0:
                for d in range(8):
                    ny, nx = y + dy[d], x + dx[d]
                    if not (0 < nx <= N and 0 < ny <= N):
                        continue
                    n_namu.append((ny,nx,1))
        '''
        # winter
        #mat_s = [[i+j for i,j in zip(mat[kka],mat_s[kka])] for kka in range(N)]
        #namus = n_namu
print('ttt', time.time()-t1)
print(len(namus))
