def solution(arr):
    min = arr[0]
    if len(arr) == 1 :
        arr.pop(0)
        return [-1]
    for i in arr :
        if min > i :
            min = i
    arr.remove(i)
    return arr

arr = [4,3,2,1]
answer = solution(arr)
print(answer)