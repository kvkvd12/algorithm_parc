import math

def solution(brown, yellow):
    # 모든 카펫 갯수
    size = brown + yellow
    # 모든 카펫 갯수의 제곱근을 1로 나눈 몫을 세로길이
    y = math.sqrt(size)//1
    # 모든 카펫 갯수를 세로길이로 나눈 값 = 가로길이
    x = size/y
    
    for i in range(size):
        # 가로길이가 정수가 될때까지 세로길이를 1씩 뺌
        if x%1 != 0:
            y -= 1
            x = size/y
        elif x%1 == 0:
            break
    
    return x, y

print(solution(24, 24))