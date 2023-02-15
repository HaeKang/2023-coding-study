import sys
input = sys.stdin.readline
n = int(input())
dic = {}
for _ in range(n):
    extension = input().split('.')[1]
    #확장자가 사전에 있으면 +1 없으면 추가
    try:
        dic[extension] += 1
    except:
        dic[extension] = 1

keys = list(dic.keys())
keys.sort()

for i in keys:
    print(i.rstrip(), dic[i])