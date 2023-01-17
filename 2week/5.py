def solution(absolutes, signs):
    sum = 0
    a = absolutes.strip("[""]").split(",")
    b = signs.strip("[""]").split(",")
    
    for i in range(len(b)):
        if b[i]=="false":
            b[i] = -1
        else:
            b[i] = 1
        sum += int(a[i])*b[i]
    return sum

print(solution(input(), input()))


# def solution(absolutes, signs):
#     sum = 0
#     a = absolutes.strip("[""]").split(",")
#     b = signs.strip("[""]").split(",")
    
#     for i in range(len(b)):
#         if b[i]=="false":
#             sum -= int(a[i])
#         else:
#             sum += int(a[i])
#     return sum, type(b[1])

# print(solution(input(), input()))


def solution(absolutes, signs):
    sum = 0
    
    for i in range(len(signs)):
        if signs[i]==0:
            sum -= absolutes[i]
        else:
            sum += absolutes[i]
    return sum

print(solution([4,7,12], [True,False,True]))