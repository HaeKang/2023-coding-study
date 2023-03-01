## 실패 (시간 초과), deque로 풀어야 한다는데 다시 풀 시간이 없었네요.. ##

def solution(rc, operations):
    for op in operations:
        if op == 'ShiftRow':
            shiftrow(rc)
        else:
            rotate(rc)
    
    return rc

def shiftrow(rc):
    n = len(rc)
    last_row = rc[n-1]
    for i in range(n-1, 0, -1):
        rc[i] = rc[i-1]
    rc[0] = last_row
    
    #test_print(rc)
    
def rotate(rc):
    n = len(rc) # row
    m = len(rc[0]) # col
    
    #test_print(rc)
    
    first_last = rc[0][m-1]
    for i in range(m-1, 0, -1): 
        rc[0][i] = rc[0][i-1]
    
    last_last = rc[n-1][m-1]
    for j in range(n-1, 1, -1):
        rc[j][m-1] = rc[j-1][m-1]
    rc[1][m-1] = first_last
    
    last_first = rc[n-1][0]
    for i in range(0, m-2):
        rc[n-1][i] = rc[n-1][i+1]
    rc[n-1][-2] = last_last
    
    #first_first = rc[0][0]
    for j in range(0, n-2):
        rc[j][0] = rc[j+1][0]
    rc[-2][0] = last_first
    
    #test_print(rc)
    
def test_print(rc):
    n = len(rc)
    for i in range(n):
        print(rc[i])
    print()