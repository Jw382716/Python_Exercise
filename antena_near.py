def solution(numbers):
    answer = [] 
    for i in range(len(numbers)) :
        a=0
        for j in range (len(numbers)) :
            if i == j :
                continue
            if numbers[i] > numbers[j] :
                a+=(numbers[i] - numbers[j])
            else :
                a+=(numbers[j] - numbers[i])
        answer.append(a)
    min = answer[0]
    for i in range(len(answer)) :
        if min > answer[i] :
            min = answer[i]
            return numbers[i]

numbers = [1,5,7,9]
answer = solution(numbers)
print(answer)