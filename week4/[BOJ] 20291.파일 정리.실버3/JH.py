import sys
from collections import Counter

N = int(input())
extensions = []
for i in range(N):
    s = sys.stdin.readline().rstrip()
    ext = s.split('.')[-1]
    extensions.append(ext)

counted = Counter(extensions) # {k, v} v는 갯수
for k in sorted(counted.keys()):
    print(k, counted[k])