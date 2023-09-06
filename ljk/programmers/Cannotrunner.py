def solution(part, com):
    answer = 0
    
    # 각 리스트를 sort 한다
    part.sort()
    com.sort()
    
    # 1중 반복문으로 해결
    for i in range(len(com)):
        if part[i] != com[i]:
            return part[i]
        
    return part[len(part)-1]