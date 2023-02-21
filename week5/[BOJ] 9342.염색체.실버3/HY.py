#^ 해당 패턴으로 시작
#? 해당 패턴을 0번또는 1번
#$ 해당 패턴으로 끝
#+ 해당 패턴이 하나 이상

import re

t = int(input())

p = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(t):
    m = p.match(input())
    if m:
        print("Infected!")
    else:
        print("Good")