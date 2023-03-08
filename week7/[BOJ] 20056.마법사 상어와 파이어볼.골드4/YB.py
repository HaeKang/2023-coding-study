import copy
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
arr = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, m, s, d = map(int, input().split())
    x, y = x-1, y-1
    arr[x][y].append([m, s, d])
# 파이어볼 m개가 각자 위치에서 이동 대기
# 질량 방향 속력 m, d, s
# 1번 n번 연결
# 8가지 방향 이동가능
for _ in range(k):
    # 1. d로 s만큼 이동 ->
    # 이동 중 같은 칸에 여러개 가능! > 리스트안에 리스트, copy
    new_arr = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not arr[i][j]:
                continue
            for ball in arr[i][j]:
                m, s, d = ball
                nx, ny = (i+dx[d]*s)%n, (j+dy[d]*s)%n
                new_arr[nx][ny].append([m, s, d])
# 2. 이동 끝난 뒤, 2개 이상 파이어볼 있는칸
     # 모두 하나로 합치고 4개로 나눔
     # nm = sum()//5
     # ns = sum()//(파이어볼 개수)
     # nd = 방향이 모두 홀수 or 모두 짝수 [0, 2, 4, 6]
            # 아니면 [1, 3, 5, 7]
    arr = copy.deepcopy(new_arr)
    for i in range(n):
        for j in range(n):
            if len(arr[i][j]) < 2:
                continue
            temp = list(map(list, zip(*arr[i][j])))

            nm, ns = sum(temp[0])//5, sum(temp[1])//len(arr[i][j])
            if nm == 0:
                arr[i][j] = []
                continue
            check_d = 0
            for d in temp[2]:
                check_d += d%2
            if check_d == len(arr[i][j]) or check_d == 0:
                nd_list = [0, 2, 4, 6]
            else:
                nd_list = [1, 3, 5, 7]
            arr[i][j] = []

            for nd in nd_list:
                arr[i][j].append([nm, ns, nd])

# k번 명령한후 남아있는 파이어볼 질량의 합
answer = 0
for i in range(n):
    for j in range(n):
        if not arr[i][j]:
            continue
        answer += sum(list(map(list, zip(*arr[i][j])))[0])
print(answer)
