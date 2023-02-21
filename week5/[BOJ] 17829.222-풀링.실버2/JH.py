import sys
N = int(input())

img = []
for i in range(N):
    img.append(list(map(int, sys.stdin.readline().rstrip().split())))

def test_print():
    for i in range(len(img)):
        print(' '.join(list(map(str, img[i]))))
    print()


def pooling():
    global img

    n = len(img)
    new_img = []

    for i in range(0, n, 2): # 2칸 씩
        new_row = []
        for j in range(0, n, 2): # 2칸 씩
            pooled = [img[i][j], img[i+1][j], img[i][j+1], img[i+1][j+1]]
            pooled.sort()
            new_row.append(pooled[2])

        new_img.append(new_row) # 새로 행렬을 만들어주기

    img = new_img


while(len(img) != 1):
    #test_print()
    pooling()

print(img[0][0])