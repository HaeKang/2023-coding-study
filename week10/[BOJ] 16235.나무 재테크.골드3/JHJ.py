N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# tree_init 리스트의 [r, c] 인덱스에 나무의 나이를 리스트로 정렬할 것
tree_init = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    tree_init[x - 1][y - 1].append(z)
nutrient_init = [[5] * N for _ in range(N)]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]


def growing(nutrient, tree):
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                tree[i][j].sort()
                tmp_tree = []  # 봄에 나이 먹는 나무
                dead = 0  # 여름에 죽은 나무
                # 계산
                for t in tree[i][j]:
                    if nutrient[i][j] >= t:
                        nutrient[i][j] -= t
                        t += 1
                        tmp_tree.append(t)
                    else:
                        dead += t // 2

                # 업데이트
                nutrient[i][j] += dead
                tree[i][j] = []
                tree[i][j].extend(tmp_tree)

    # 가을
    for i in range(N):
        for j in range(N):
            if tree[i][j]:
                for t in tree[i][j]:
                    if t % 5 == 0:
                        for w in range(8):
                            nx, ny = i + dx[w], j + dy[w]
                            if 0 <= nx < N and 0 <= ny < N:
                                tree[nx][ny].append(1)


    # 겨울
    for i in range(N):
        nutrient[i] = [x + y for x, y in zip(nutrient[i], A[i])]


for _ in range(K):
    growing(nutrient_init, tree_init)


anw = 0
for i in range(N):
    for j in range(N):
        anw += len(tree_init[i][j])

print(anw)