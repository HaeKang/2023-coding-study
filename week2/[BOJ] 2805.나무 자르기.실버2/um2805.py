import sys


def checker(dat,wl,st,en,delta):
    for kka in range(st, en, delta):
        sol = 0
        for kki in range(dat[0][0]):
            if dat[1][-kki - 1] <= kka:
                break
            else:
                sol += dat[1][-kki - 1] - kka
        if sol >= wl:
            print(kka)
            break


def bs(dat,sp):
    sol = 0
    for kki in range(dat[0][0]):
        if dat[1][-kki-1] <= sp:
            break
        else:
            sol += dat[1][-kki-1] - sp
    return sol

def namu(dat):
    l = 0
    dat[1].sort()
    wl = dat[0][1]
    sp = int(dat[1][-1]/2)
    sol = 0
    b_sp = [1,dat[1][-1]]
    while(True):
        sol = bs(dat,sp)
        #print(sol, ' ' , sp)
        if sol == wl:
            print(sp)
            return True
        elif sol > wl:
            b_sp[0] = sp
            sp = int((sp + b_sp[1])/2)
        else:
            b_sp[1] = sp
            sp = int((sp + b_sp[0])/2)
        if (0 < sol - wl <= 2) or (0 < wl - sol <= 2):
            break


    if sol > wl:
        checker(dat,wl,dat[1][-1],sp,-1)
    else:
        checker(dat,wl,sp,1,-1)

dat = list()
for kka in range(2):
    dat.append(list(map(int,sys.stdin.readline().split())))

namu(dat)