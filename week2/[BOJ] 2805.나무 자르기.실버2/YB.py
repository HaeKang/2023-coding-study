n, m = map(int, input().split())
trees = list(map(int, input().split()))

st, end = 0, max(trees)
answer = 0

while st<=end:
    mid = (st+end)//2
    total = 0
    for tree in trees:
        total += max(0, tree-mid)
    if total < m:
        end = mid-1
    else:
        answer = max(answer, mid)
        st = mid+1
print(answer)
