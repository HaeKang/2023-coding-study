r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]


# 등장 횟수가 커지는 순
# (여러가지면) 수가 커지는 순
# 커지는 순으로 정렬한다 == 123(o) 321(x)

# 연산 수행
def calculate(matrix, sort='R'):
    """
    행렬 연산 수행
    :param sort: R or C
    :return: 연산 수행 후, 변환된 행렬 반환
    """
    ret = []  # return
    max_length = 0
    for row in matrix:
        cnt_list = []  # append (수, 개수) = (num, cnt)
        nrow = []  # ret에 append할 new row = nrow
        for num in set(row):
            if num == 0: continue
            cnt = row.count(num)
            cnt_list.append((num, cnt))
        cnt_list = sorted(cnt_list, key=lambda x: [x[1], x[0]])
        for num_cnt in cnt_list:
            nrow.extend(num_cnt)
        ret.append(nrow)
        max_length = max(max_length, len(nrow))

    for row in nrow:
        row += [0] * (max_length - len(row))
        if len(row) > 100:
            row = row[:100]

    return list()

    pass


print(A[1][1])
print(type(A[1][1]))