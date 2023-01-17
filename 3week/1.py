def solution(s):
    p_answer = []
    y_answer = []
    for answer in s.lower():
        if answer == "p":
            p_answer.append(answer)
        elif answer == "y":
            y_answer.append(answer)
            
    if len(p_answer) == 0 and len(y_answer) == 0:
        return True
    elif len(p_answer) == len(y_answer):
        return True
    else:
        return False

print(solution("ikppYyyi"))