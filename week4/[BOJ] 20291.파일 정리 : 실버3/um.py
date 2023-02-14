import sys

in_d = sys.stdin.readline
N = int(in_d())
dat = [str(in_d()).split('.')[1].split('\n')[0] for _ in range(N)] # . 기준 확장자만 잘라서 저장
dat.sort()
out = [dat[0]]
out_c = [0]
for kka in range(N):
    if dat[kka] == out[-1]: # 마지막에 추가한 확장자와 동일하면 출력 카운트 추가
        out_c[-1] += 1
    else:
        out_c.append(1) # 다르면 확장자 추가
        out.append(dat[kka])

for kka in range(len(out)):
    print(out[kka],out_c[kka])