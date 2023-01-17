def solution(num):
    i = 0
    for i in range(501):
        if i == 500:
            return -1
        elif num == 1:
            return i
        elif num % 2 == 0:
            num = num / 2
            i += 1
        elif num % 2 == 1:
            num = num*3 + 1
            i += 1
        
print(solution(626331))