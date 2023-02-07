import sys

in_d = sys.stdin.readline
N = int(in_d())
dat = list(map(int, in_d().split()))
ber = int(in_d())
dat.sort()

#print(dat)
mi = 0
ma = dat[-1]
getsu = len(dat)

def bs():
    global mi, ma, getsu, dat, ber
    md = int((mi + ma)/2)
    val = 0
    for kka in range(getsu):
        if md <= dat[kka]:
            val += (getsu - kka) * md
            break
        else:
            val += dat[kka]

        if val > ber:
            break

    if val > ber:
        ma = md - 1
    elif val == ber:
        return md
    else:
        mi = md + 1
def run():
    global mi,ma
    while(mi <= ma):
        val = bs()
        if val:
            ma = val
            break
    print(ma)
val = 0
for kka in range(getsu):
    val += dat[kka]
if val <= ber:
    print(dat[-1])
#elif dat[-1] < 0:
#    print('0')
else:
    run()