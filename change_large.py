def solution(k, a, b):
    answer = 0
    a.sort()
    b.sort(reverse=True)
    
    for i in range(k) :
        if a[i] > b[i] :
            continue
        else :
            a[i] = b[i]
    for i in a :
        answer += i
    return answer

k = 3
a = [1,2,5,4,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)
