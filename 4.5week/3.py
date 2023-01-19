from itertools import permutations

def solution(answers):
    # 주어진 값 하나하나 리스트에 추가
    a = list(answers)
    b = []
    c = []
    # 리스트에 담겨있는 숫자 조합
    for i in range(len(answers)):
        b.append(list(permutations(a, i+1)))
    # 그 값들을 모두 소수 판별해서 c에 추가
    for i in range(len(b)):
        for j in range(len(b[i])):
            for k in range(2, int(''.join(b[i][j]))):
                if int(''.join(b[i][j])) % k == 0:
                    break
                else:
                    c.append(int(''.join(b[i][j])))
                    break
    # 중복되는 값 빼고 갯수
    return len(set(c))

print(solution("17"))
