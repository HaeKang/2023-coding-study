def check1(s, i):   #짝수인 경우
    left = i - 1
    right = i
    cnt = 0
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            cnt += 2
            left -= 1
            right += 1
        else:
            break
    return cnt

def check2(s, i):  #홀수인 경우
    left = i - 1
    right = i + 1
    cnt = 1
    while left >= 0 and right < len(s):
        if s[left] == s[right]:
            cnt += 2
            left -= 1
            right += 1
        else:
            break
    return cnt

def solution(s):
    ans = 0
    for i in range(len(s)):
        ans = max(ans, check1(s, i))
        ans = max(ans, check2(s, i))
    return ans