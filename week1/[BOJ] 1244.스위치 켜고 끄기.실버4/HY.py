def change(x):
    switch[x] = abs(switch[x] - 1)


def man(x):
    for i in range(x, n + 1, x):
        change(i)


def woman(x):
    change(x)
    for i in range(1, n + 1):
        if x - i <= 0 or x + i >= n + 1:
            break

        if switch[x - i] == switch[x + i]:
            change(x - i)
            change(x + i)
        else:
            break


n = int(input())
switch = [0] + list(map(int, input().split()))
num = int(input())
s = []
for _ in range(num):
    s.append(list(map(int, input().split())))

for i in range(num):
    if s[i][0] == 1:
        man(s[i][1])
    else:
        woman(s[i][1])

tmp = 0
for i in switch[1:]:
    print(i, end=' ')
    tmp += 1
    if tmp == 20:
        print()
        tmp = 0