n = int(input())
dict = {}

for _ in range(n):
    fname = input().split(".")
    if fname[1] in dict:
        dict[fname[1]] = dict[fname[1]] + 1
    else:
        dict[fname[1]] = 1

keys = list(dict.keys())
keys.sort()
for key in keys:
    print(key, dict[key])
