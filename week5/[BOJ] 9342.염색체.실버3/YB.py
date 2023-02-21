def check(now):
    for ch in ['A', 'F', 'C']:
        if now and now[0] == ch:
            idx=len(now)-1
            for i in range(len(now)):
                if now[i] != ch:
                    idx = i
                    break
            now = now[idx:]
        else:
            return False

    if not now or (len(now) == 1 and now[0] in ['A', 'B','C','D','E','F']):
        return True

    else:
        return False
n = int(input())

for _ in range(n):
    now = [s for s in input()]

    answer = False
    if now[0] in ['B', 'C','D','E','F']:
        temp = check(now[1:])
        if temp:
            print('Infected!')
            continue
    elif now[0] == 'A':
        temp = check(now)
        if temp:
            print('Infected!')
            continue

    print('Good')
