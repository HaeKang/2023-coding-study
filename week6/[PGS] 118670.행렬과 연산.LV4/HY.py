from collections import deque

def solution(rc, operations):
    answer = []
    #왼쪽, 가운데, 오른쪽 따로 구하기
    left = deque([rc[i][0] for i in range(len(rc))])
    right = deque([rc[i][-1] for i in range(len(rc))])
    mid = deque([deque(rc[i][1:-1]) for i in range(len(rc))])
    
    for operation in operations:
        if operation == "ShiftRow":
            mid.rotate(1)
            left.rotate(1)
            right.rotate(1)
            
        else:
            mid[0].appendleft(left.popleft())
            right.appendleft(mid[0].pop())
            mid[-1].append(right.pop())
            left.append(mid[-1].popleft())
            
    for i in range(len(rc)):
        answer.append([left[i]] + list(mid[i]) + [right[i]])
        
    return answer