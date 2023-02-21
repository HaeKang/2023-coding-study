saw = []
for i in range(4):
    row = input().rstrip()
    new_row = []
    for c in row:
        new_row.append(c)
    saw.append(new_row)

def test_print(k):
    global saw
    print(saw[k])
    print()

def change_dir(dir):
    if dir == -1:
        return 1
    else:
        return -1

def rotate(no, dir):
    global saw

    if dir == 0:
        return

    if dir == 1: # 시계 방향 ->
        last = saw[no][7]
        for i in range(7, 0, -1):
            saw[no][i] = saw[no][i-1]
        saw[no][0] = last

    else: # 반시계 <-
        first = saw[no][0]
        for i in range(7):
            saw[no][i] = saw[no][i+1]
        saw[no][7] = first


K = int(input())
for i in range(K):
    no, dir = map(int, input().split())
    no -= 1 # idx

    dirs = [0] * 4
    dirs[no] = dir

    j = 1
    while(no + j < 4):
        if saw[no+j][-2] != saw[no+j-1][2] and dirs[no+j-1] != 0:
            dirs[no+j] = change_dir(dirs[no+j-1])
        j += 1

    j = 1
    while(no - j >= 0):
        if saw[no-j][2] != saw[no-j+1][-2] and dirs[no-j+1] != 0:
            dirs[no-j] = change_dir(dirs[no-j+1])
        j += 1
    for n, dir in enumerate(dirs):
        rotate(n, dir)

score = 0
for i in range(4):
    if saw[i][0] == '1':
        score += 2**i
print(score)