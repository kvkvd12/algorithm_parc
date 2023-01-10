def solution(N, stages):
    answer = []
    for i in range(1, N+1):
        fail = []
        for j in range(len(stages)):
            if i>=stages[j]:
                fail.append(stages[j])
        answer.append(len(fail)/N)    
    
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))