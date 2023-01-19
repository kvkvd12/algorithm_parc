# def solution(answers):
#     a, b, c, answer=[], [], [], []
#     a_correct, b_correct, c_correct = 0, 0, 0
#     for i in range(1):
#         a.extend([1, 2, 3, 4, 5])
#     for i in range(1):
#         b.extend([2, 1, 2, 3, 2, 4, 2, 5])
#     for i in range(1):
#         c.extend([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
#     for i in range(1):
#         answer.extend(answers)
        
#     for i in range(len(answer)):
#         if a[i] == answer[i]:
#             a_correct += 1
#         if b[i] == answer[i]:
#             b_correct += 1
#         if c[i] == answer[i]:
#             c_correct += 1
#     correct = [a_correct, b_correct, c_correct]
#     top = []
#     for i in range(3):
#         if correct[i]>=max(correct):
#             top.append(i+1)
#     return top

# print(solution([1,3,2,4,2]))


def solution(answers):
    a, b, c, answer, correct, top = [], [], [], [], [0,0,0], []
    # 1,2,3번 수포자들의 찍는 방식을 리스트에 추가, 정답배열 리스트에 추가
    for i in range(1):
        a.extend([1, 2, 3, 4, 5])
    for i in range(1):
        b.extend([2, 1, 2, 3, 2, 4, 2, 5])
    for i in range(1):
        c.extend([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    for i in range(1):
        answer.extend(answers)
    
    # 정답과 1,2,3이 찍은 답 비교해서 정답갯수 추가
    for i in range(len(answer)):
        if a[i] == answer[i]:
            correct[0] += 1
        if b[i] == answer[i]:
            correct[1] += 1
        if c[i] == answer[i]:
            correct[2] += 1
    # 정답갯수 리스트 중 제일 큰값보다 크거나 같으면 top리스트에 추가
    for i in range(3):
        if correct[i]>=max(correct):
            top.append(i+1)
    return top

print(solution([1,2,3,4,5]))