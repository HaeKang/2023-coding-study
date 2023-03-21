import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]
ans = -1

# 100초
for t in range(101):
    if r-1 < len(arr) and c-1 < len(arr[0]):
        if arr[r-1][c-1] == k:
            ans = t
            break

    row_len = len(arr)
    col_len = len(arr[0])

    # R연산
    if row_len >= col_len:
        tmp = []
        max_len = 0  # 최대 길이
        dict = {}
        for i in range(row_len):
            dict.clear()
            for j in range(col_len):
                if arr[i][j] != 0:
                    if arr[i][j] in dict:
                        dict[arr[i][j]] = dict.get(arr[i][j]) + 1
                    else:
                        dict[arr[i][j]] = 1

            tmp2 = sorted(dict.items(), key=lambda x: (x[1], x[0]))

            tmp3 = ()
            for t in tmp2:
                tmp3 += t

            if len([*tmp3]) > max_len:
                max_len = len([*tmp3])
            tmp.append([*tmp3])

        for i in range(0, len(tmp)):
            if len(tmp[i]) < max_len:
                tmp[i] = tmp[i] + ([0] * (max_len - len(tmp[i])))

        arr = tmp

    # C연산
    else:
        tmp = []
        max_len = 0  # 최대 길이
        dict = {}

        for j in range(col_len):
            dict.clear()
            for i in range(row_len):
                if arr[i][j] != 0:
                    if arr[i][j] in dict:
                        dict[arr[i][j]] = dict.get(arr[i][j]) + 1
                    else:
                        dict[arr[i][j]] = 1

            tmp2 = sorted(dict.items(), key=lambda x: (x[1], x[0]))
            tmp3 = ()
            for t in tmp2:
                tmp3 += t

            if len([*tmp3]) > max_len:
                max_len = len([*tmp3])
            tmp.append([*tmp3])

        for i in range(0, len(tmp)):
            if len(tmp[i]) < max_len:
                tmp[i] = tmp[i] + ([0] * (max_len - len(tmp[i])))

        arr = list(map(list, zip(*tmp)))

print(ans)
