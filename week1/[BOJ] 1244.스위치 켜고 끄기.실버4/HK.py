# 스위치 값 변경
def change_val(val):
    if val == '0':
        return '1'
    else:
        return '0'

# 남학생


def man_case(num, arr, switch):
    for i in range(num, switch, num + 1):
        arr[i] = change_val(arr[i])

    return arr

# 여학생


def women_case(num, arr, switch):
    start_idx = num - 1
    end_idx = num + 1

    arr[num] = change_val(arr[num])

    while start_idx >= 0 and end_idx <= switch-1:
        if arr[start_idx] == arr[end_idx]:
            arr[start_idx] = change_val(arr[start_idx])
            arr[end_idx] = change_val(arr[end_idx])
            start_idx -= 1
            end_idx += 1
        else:
            break

    return arr


switch = int(input())
arr = list(input().split(" "))

t = int(input())

for _ in range(t):
    sex, num = map(int, input().split(" "))
    if sex == 1:
        arr = man_case(num - 1, arr, switch)
    else:
        arr = women_case(num - 1, arr, switch)

cnt = 1
for data in arr:
    print(data, end=" ")
    if cnt % 20 == 0:
        print()
    cnt += 1
