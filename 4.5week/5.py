def solution(k, dungeons):
    clear = 0
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k:
            k -= dungeons[i][1]
            clear += 1
        elif k == 0:
            return clear
        elif dungeons[i][0] > k:
            pass
        
    return clear

print(solution(80, [[80,20],[50,40],[30,10]]))