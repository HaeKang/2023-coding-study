import copy

dat = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]
n = 9

dat = [[1,2],[2,3],[3,4]]
n = 4
def solution(n, wires_ori):
    res = list()
    for kka in range(n-1): # 각 인덱스 끊어봄
        team1, team2 = set(), set()  # 두 팀으로 나눔 set 이용 겹침 허용 안하기때문
        #print(kka)
        wires = copy.deepcopy(wires_ori) # 카피밖에 생각안나서 사용. 함수 입력 복사 후
        team1.update([wires[kka][0]]) # 끊을 원소 팀에 배정후
        team2.update([wires[kka][1]])
        del wires[kka] # 원소 지움
        while len(team1) + len(team2) < n: # 팀의 수의 합이 전체 수와 같아질때까지
            for dd in wires: # 하나 빠진 전력망에서
                team1_temp = list()
                for t1 in team1: # 각팀의 원소 모두 불러서
                    if t1 in dd: # 하나빠진 전력망에 해당하는 송전탑있는지확인
                        team1_temp += dd
                team1.update(team1_temp) # 추가
                team2_temp = list()
                for t2 in team2:
                    if t2 in dd:
                        team2_temp += dd
                team2.update(team2_temp)
        #print(team1, 'vs', team2)
        res.append(abs(len(team1) - len(team2)))
    #print(res)
    return min(res)


print(solution(n,dat))