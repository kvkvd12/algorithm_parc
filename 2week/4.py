def solution(n):
    for i in range(2,n):
        remainder = n%i
        if remainder == 1:
            return i

print(solution(int(input())))