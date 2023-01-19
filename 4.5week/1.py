# def solution(sizes):
#     a = [sizes[0][0],sizes[0][1]]
    
#     for size in sizes:
#         if a[0]<size[0]:
#             a[0]=size[0]
#     for size in sizes:
#         if a[1]<size[1]:
#             a[1]=size[1]
                    
#     return a[0]*a[1], a

# print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))




def solution(sizes):
    a = []
    b = []
    c = []
    # 가로길이, 세로길이 모음
    for size in sizes:
        a.append(size[0])
    for size in sizes:
        b.append(size[1])
    # 가로 세로 중에 가로가 제일 길다면
    if max(a)>max(b):
        for i in range(len(a)):
            # 그중에서 세로가 더 짧은 길이들만 c에 추가
            if a[i] > b[i]:
                c.append(b[i])
        # 가장 긴 가로와 가장 긴 세로의 곱
        return max(a)*max(c)
    
    elif max(a)==max(b):
        return max(a)*max(b)
    
    else:
        for i in range(len(a)):
            if a[i] < b[i]:
                c.append(a[i])
        return max(b)*max(c)

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))