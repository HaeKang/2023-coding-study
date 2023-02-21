import sys
input = sys.stdin.readline

n, m = map(int, input().split())

names = []
vals = []

for _ in range(n):
    name, val = input().split()

    if len(vals) > 0:
        if vals[-1] == val:
            continue

    names.append(name)
    vals.append(int(val))


def binary_search(t):
    left = 0
    right = len(vals) - 1

    while left <= right:
        mid = (left + right) // 2

        if t > vals[mid]:
            left = mid + 1
            mid = left
        else:
            right = mid - 1

    print(names[mid])


for _ in range(m):
    target = int(input())
    binary_search(target)
