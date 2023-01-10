def solution(d, budget):
    for i in range(len(d)):
        if sum(d) > budget:
            answer = sum(d)-d[i]
    return answer

print(solution([1,3,2,5,4], 9))