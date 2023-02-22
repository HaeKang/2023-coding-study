import sys
T = int(input())

def is_pass(s):
    
    i = 0
    n = len(s)

    # case 1
    if s[i] in 'BCDEF':
        i += 1
    elif s[i] == 'A':
        pass
    else:
        return False # 나머지 경우

    # case 2
    while(i < n and s[i] == 'A'):
        i += 1
    if i == n:
        return False

    # case 3
    while(i < n and s[i] == 'F'):
        i += 1
    if i == n:
        return False

    # case 4
    while(i < n and s[i] == 'C'):
        i += 1

    # case 5
    if i == n:
        return True

    if i+1 == n and s[i] in 'ABCDEF':
        return True
    
    return False


ret = []
for i in range(T):
    s = sys.stdin.readline().rstrip()

    if is_pass(s):
        ret.append("Infected!")
    else:
        ret.append("Good")

for i in range(T):
    print(ret[i])