from collections import deque

gear = []
gear.append(deque(list(map(int, input()))))
gear.append(deque(list(map(int, input()))))
gear.append(deque(list(map(int, input()))))
gear.append(deque(list(map(int, input()))))

#톱니바퀴 돌리는 함수
def clock(g):
    gear[g - 1].rotate(1)

def counter_clock(g):
    gear[g - 1].rotate(-1)
    
k = int(input())
for _ in range(k):
    g, d = map(int, input().split())
    
    #톱니가 겹치는 부분을 리스트에 넣고 확인
    check_list = [[] for _ in range(3)]
    for i in range(3):
        check_list[i].append(gear[i][2])
        check_list[i].append(gear[i + 1][6])
    
    #회전시키려는 톱니바퀴 먼저 회전
    if d == 1:
        clock(g)
    else:
        counter_clock(g)
        
    #왼쪽 체크하기
    check_d = d * -1  #반대로 돌아가기 때문에 회전 방향 확인용
    if g != 1:  
        for i in range(g - 1, 0, -1):
            if check_list[i - 1][0] != check_list[i - 1][1]:
                if check_d == 1:
                    clock(i)
                    check_d = -1
                else:
                    counter_clock(i)
                    check_d = 1
            else:
                break
                
    #오른쪽 체크하기            
    check_d = d * -1           
    if g != 4:  
        for i in range(g - 1, 3):
            if check_list[i][0] != check_list[i][1]:
                if check_d == 1:
                    clock(i + 2)
                    check_d = -1
                else:
                    counter_clock(i + 2)
                    check_d = 1
            else:
                break
                
ans = 0
if gear[0][0] == 1:
    ans += 1
if gear[1][0] == 1:
    ans += 2
if gear[2][0] == 1:
    ans += 4
if gear[3][0] == 1:
    ans += 8
    
print(ans)