import sys
from collections import Counter

d_in = sys.stdin.readline
T = int(d_in())

def chk(dat):
    trig_A,trig_F,trig_C = False,False,False
    if dat[0] not in ['A','B','C','D','E','F']:
        return False
    cc = Counter(dat) # coounter 가 넣은 순서대로 출력하기 때문에 사용
    for key,value in cc.items():
        if key == 'A' and not trig_A:
            trig_A = True
            continue

        if trig_A and not trig_F and not trig_C:
            if key == 'F':
                trig_F = True
                continue
            else :
                return False
        if trig_F and not trig_C:
            if key == 'C':
               trig_C = True
               continue
            else:
                return False
        if trig_C and key not in ['A','B','C','D','E','F']:
            return False
    if trig_C:
        return True
    return False

for t in range(T):
    dd = str(d_in()).split('\n')[0]
    #print(dd)
    o = chk(dd)
    if o:
        print("Infected!")
    else:
        print('Good')
