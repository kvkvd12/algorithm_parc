def solution(a, b):
    if a == b:
        return a
    else:
        count = abs(a-b)+1
        sum = 0
        if a > b:
            for i in range(count):
                sum += b + i
            return sum
        else:
            for i in range(count):
                sum += a + i
            return sum
                
print(solution(int(input()), int(input())))