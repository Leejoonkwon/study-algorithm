def solution(nums):
    answer = 0
    # 폰켓몬 고유넘버 
    unique_mon = len(set(nums))
    
    # N마리의 폰켓몬 2로 나눈 수
    even_num = len(nums)/2
    
    # N마리의 폰켓몬을 2로 나눈 값보다
    # 유니크가 클 경우 2로 나눈 값 반환
    if even_num < unique_mon : 
        return even_num
    
    return unique_mon
