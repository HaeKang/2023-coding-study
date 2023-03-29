import sys

in_d = sys.stdin.readline
N = int(in_d())
sik = in_d().split()[0]
nums, ops = list(), list()
trig = True
for i in range(N):
    if trig:
        nums.append(int(sik[i]))
        trig = False
    else:
        trig = True
        ops.append(sik[i])
#print(nums,ops)
opN = len(ops)
res = set()

def _cal(o,a,b):
    if o == '+': return a+b
    elif o == '-': return a-b
    else: return a*b

def cal(idx):
    global res, ops
    val = 0
    #print('www',idx)
    nops, nnums = list(), list()
    for kka in range(opN): # 괄호 먼저 연산
        if kka in idx:
            val = _cal(ops[kka],nums[kka],nums[kka+1])
            nnums.append(val)
        else:
            nops.append(ops[kka])
            if kka - 1 not in idx:
                nnums.append(nums[kka])
            if kka == opN - 1 :
                nnums.append(nums[kka+1])

    for kka in range(len(nops)): # 순서대로 연산
        if kka == 0:
            val = _cal(nops[kka],nnums[kka],nnums[kka+1])
        else:
            val = _cal(nops[kka],val,nnums[kka+1])
    res.add(val)
    return 0

def dfs(n,op_idx):
    global opN
    if n > opN - 1:
        return cal(op_idx)
    # use
    op_idx.append(n)
    #print('sgsgs',op_idx)
    dfs(n+2,op_idx)
    op_idx.pop()
    # not use
    dfs(n+1,op_idx)

if N == 1:
    print(nums[0])
else:
    dfs(0,list())
    #print(res)
    print(max(res))