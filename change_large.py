def solution(k, a, b):
    answer = 0
    a.sort()
    b.sort(reverse=True)
    
    for i in range(k) :
        a[i] = b[i]
    for i in a :
        answer += i
    return answer

k = 3
a = [5,7,8,8,3]
b = [5,5,6,6,5]
answer = solution(k, a, b)
print(answer)
