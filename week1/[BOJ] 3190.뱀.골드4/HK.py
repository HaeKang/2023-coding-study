import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [['E'] * (n+1) for _ in range(n+1)]

for _ in range(int(input())):
    r1, c1 = map(int, input().split(" "))
    arr[r1][c1] = 'A'  # 사과

dict = {}   # key : 시간, value : 방향(D,L)
for _ in range(int(input())):
    sec, dir = input().split()
    dict[int(sec)] = dir


dr = [1, -1, 0, 0]  # 하 상
dc = [0, 0, -1, 1]  # 좌 우

s_r, s_c = 1, 1  # 뱀 초기 위치
s_dir = 3   # 초기 방향 (우)

time = 0
arr[s_r][s_c] = 'S'  # 뱀 초기 위치 설정

# 뱀 좌표 기록
q = deque()
q.append([s_r, s_c])

while True:
    time += 1

    # 이동
    n_r = s_r + dr[s_dir]
    n_c = s_c + dc[s_dir]

    # 범위체크
    if n_r > n or n_c > n or n_r < 1 or n_c < 1:
        print(time)
        break
    # 뱀 위치 체크
    elif arr[n_r][n_c] == 'S':
        print(time)
        break

    # 사과 아닌 케이스 처리
    if arr[n_r][n_c] != 'A':
        t_r, t_c = q.popleft()  # 꼬리 위치
        arr[t_r][t_c] = 'E'  # 꼬리 삭제

    arr[n_r][n_c] = 'S'  # 뱀 위치 설정
    q.append([n_r, n_c])    # 뱀 위치 queue에 넣음

    s_r = n_r
    s_c = n_c

    # 방향 바꾸기
    if time in dict.keys():
        # 0 : 하 1: 상 2: 좌 3: 우

        # 오른쪽
        if dict[time] == 'D':
            # 하 -> 좌
            if s_dir == 0:
                s_dir = 2

            # 상 -> 우
            elif s_dir == 1:
                s_dir = 3

            # 좌 -> 상
            elif s_dir == 2:
                s_dir = 1

            # 우 -> 하
            else:
                s_dir = 0

        # 왼쪽
        else:
            # 하 -> 우
            if s_dir == 0:
                s_dir = 3

            # 상 -> 좌
            elif s_dir == 1:
                s_dir = 2

            # 좌 -> 하
            elif s_dir == 2:
                s_dir = 0

            # 우 -> 상
            else:
                s_dir = 1
