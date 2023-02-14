N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))

minimum = 1E+12
maximum = -minimum

def check_all_used():
    global ops
    for o in ops:
        if o >= 1:
            return False
    return True

def get(ret, k): # ret : 현재 값, k : 인덱스
    global nums, ops, minimum, maximum

    if check_all_used():
        maximum = max(ret, maximum)
        minimum = min(ret, minimum)
        return

    for i in range(4):
        if ops[i] >= 1:

            ops[i] -= 1

            if i == 0:
                get(ret+nums[k], k+1)
            elif i == 1:
                get(ret-nums[k], k+1)
            elif i == 2:
                get(ret*nums[k], k+1)
            else:
                if ret < 0: get(-((-ret)//nums[k]), k+1)
                else: get(ret//nums[k], k+1)

            ops[i] += 1

get(nums[0], 1)

print(maximum)
print(minimum)