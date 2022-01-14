def solution(n) :
    answer = 0
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else : 
        answer = solution(n-1) + solution(n-2)
        
    return answer
answer = solution(10)
print(answer)
