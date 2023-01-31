"""
https://www.acmicpc.net/problem/14499

지도의 각 칸에는 정수가 하나씩 쓰여져 있다. 주사위를 굴렸을 때, 
이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다. 
0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.

주사위를 놓은 곳의 좌표와 이동시키는 명령이 주어졌을 때, 주사위가 이동했을 때 마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.

주사위는 지도의 바깥으로 이동시킬 수 없다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

첫째 줄에 지도의 세로 크기 N(row), 가로 크기 M(col) (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 
주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

4 2 0 0 8
0 2
3 4
5 6
7 8
4 4 4 1 3 3 3 2

0
0
3
0
0
8
6
3

"""

# idx : 0 -> 아랫면 idx : 5 -> 윗면
dice = {}
dice[0] = 1  # 아래
dice[1] = 2  # 북쪽 옆면
dice[2] = 3  # 동쪽 옆면
dice[3] = 4  # 서쪽 옆면
dice[4] = 5  # 남쪽 옆면
dice[5] = 6  # 위

# 동쪽 이동
# 동쪽 옆면 -> 아래, 서쪽 옆면 -> 위
# 아래 -> 서쪽 옆면, 위 -> 동쪽 옆면
# 북쪽 옆면 -> 북쪽 옆면, 남쪽 옆면 -> 남쪽 옆면


def move_right(param_dice):
    new_dice = {}

    # 동쪽 옆면 -> 아래
    new_dice[0] = param_dice[2]

    # 서쪽 옆면 -> 위
    new_dice[5] = param_dice[3]

    # 북쪽 옆면 동일
    new_dice[1] = param_dice[1]

    # 남쪽 옆면 동일
    new_dice[4] = param_dice[4]

    # 아래 -> 서쪽 옆면
    new_dice[3] = param_dice[0]

    # 위 -> 동쪽 옆면
    new_dice[2] = param_dice[5]

    return new_dice


# 서쪽 이동
# 서쪽 옆면 -> 아래, 동쪽 옆면 -> 위
#
def move_left(param_dice):
    new_dice = {}

    # 서쪽 옆면 -> 아래
    new_dice[0] = param_dice[3]

    # 동쪽 옆면 -> 위
    new_dice[5] = param_dice[2]

    # 북쪽 옆면 동일
    new_dice[1] = param_dice[1]

    # 남쪽 옆면 동일
    new_dice[4] = param_dice[4]

    # 아래 -> 동쪽옆면
    new_dice[3] = param_dice[0]

    # 위 -> 서쪽옆면
    new_dice[2] = param_dice[5]

    return new_dice

# 북쪽 이동

# 남쪽 이동


n, m, d_r, d_c, k = map(int, input().split())
arr = []

# 배열
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 이동횟수
move = []
move.append(list(map(int, input().split())))


dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
