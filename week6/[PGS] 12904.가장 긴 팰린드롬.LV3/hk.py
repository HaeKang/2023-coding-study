def solution(s):
    answer = 1

    for i in range(len(s)):
        for j in range(len(s)-1, i, -1):
            if s[i] != s[j]:
                continue

            # 효율성테스트
            if len(s) - i < answer:
                break

            # tmp_lst = list(s[i:j+1])
            # tmp_lst.reverse()
            # tmp_lst = ''.join(tmp_lst)

            # 효율성테스트로 인해 인덱스로 풀었음
            if s[i:j+1] == s[i:j+1][::-1]:
                if len(s[i:j+1]) == len(s):
                    return len(s)

                answer = max(answer, len(s[i:j+1]))
                break   # 효율성테스트


#             mid = (j - i) // 2

#             # 홀수 팰린드롬 케이스
#             if (j - i) % 2 == 0:
#                 tmp_lst = list(s[mid+1 : j+1])
#                 tmp_lst.reverse()
#                 tmp_lst = ''.join(tmp_lst)
#                 print(i, j, mid, s[i:mid], " ", tmp_lst)
#                 if s[i:mid] == tmp_lst:
#                     answer = max(answer, len(s[i:j+1]))

#             # 짝수 팰린드롬 케이스
#             else:
#                 tmp_lst = list(s[mid : j+1])
#                 tmp_lst.reverse()
#                 tmp_lst = ''.join(tmp_lst)
#                 print(i, j, mid, s[i:mid+1], " ", tmp_lst)
#                 if s[i:mid+1] == tmp_lst:
#                     answer = max(answer, len(s[i:j+1]))
    return answer
