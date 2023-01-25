# 1은 켜짐, 0은 꺼짐
#학생들에게 1<= <= 스위치 개수 자연수 줌
# 남: 스위치 번호 %(번호) == 0: 스위치 상태 바꿈
# 여: 받은 수와 같은 번호가 붙은 스위치를 중심으로, 좌우 대칭이면서 가장 많은 스위치를
#포함하는 구간 찾아서 그 구간의 스위치 상태 모두 바꿈,
# 구간에 속하는 스위치 개수는 항상 홀수
n = int(input())
arr = list(map(int, input().split()))
stu_num = int(input())
students = []
for _ in range(stu_num):
    students.append(list(map(int, input().split()))) #남자면 1 여자면 2

def do_boy(num):
    global arr
    for i in range(n):
        if (i+1)%num == 0:
            if arr[i] == 1:
                arr[i] = 0
            else:
                arr[i] = 1
    return
def do_girl(num):
    left, right = num-1, num-1
    while 0<= left < n and 0<= right < n:
        if arr[left] == arr[right]:
            if arr[left] == 1:
                arr[left] = 0
                arr[right] = 0
            else:
                arr[left] = 1
                arr[right] = 1
        else:
            break
        left -= 1
        right += 1
    return

for gender, num in students:
    if gender == 1:
        do_boy(num)
    else:
        do_girl(num)

for i in range(n//20+1):
     print(' '.join(map(lambda x:str(x), arr[i*20:min(i*20+20, n)])))


