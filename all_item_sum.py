def solution(numbers):
    answer = []
    for i in range(len(numbers)) :
        for j in range (len(numbers)) :
            if i == j :
                continue
            a = numbers[i] + numbers[j]
            answer.append(a)
    answer = set(answer)
    return answer

numbers = [2,1,3,4,1]
answer = solution(numbers)
print(answer)