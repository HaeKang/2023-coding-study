import sys

N = int(sys.stdin.readline().split()[0])
dat = list(map(int, sys.stdin.readline().split()))

dat.sort()
print(dat[-1]+dat[-2])
#print(N,'  ',dat)