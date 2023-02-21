import sys

in_d = sys.stdin.readline
N = int(in_d())
dat = list(map(int,in_d().split()))
res = -1

res = {str(dat[0]) : 1} # 기준(이전) dict
for n in range(1,N-1): # 마지막 = 전까지 + - 각각
    nres = dict()
    for key,val in res.items(): # 새로운 dict 에 기준(이전) dict(res) 의 키 값들을 더해봄 (nval)
        nval = int(key) + dat[n]
        if 0 <= nval <= 20:
            if str(nval) not in nres: # 새로운 dict에 nval 없으면 키값으로 추가
                nres[str(nval)] = val
            else: # 새로운 dict에 nval 있으면 키값에 기준 dict 의 val 더함.
                nres[str(nval)] += val

        nval = int(key) - dat[n] # - 연산 위와 동일
        if 0 <= nval <= 20:
            if str(nval) not in nres:
                nres[str(nval)] = val
            else:
                nres[str(nval)] += val
    #print('+++++++++++++++++++++++++')
    #print(res)
    #print('---')
    #print(nres)
    res = nres

tot = 0
for key,val in nres.items():
    #print(key, val)
    if int(key) == dat[-1]:
        tot += val
print(tot)