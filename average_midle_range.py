n = int(input('갯수 입력 :'))
data = []
for i in range(n):
    data.append(int(input('수입력 :')))
summ = 0
for i in data :
    summ += i
print(f'산술평균 : {summ/len(data)}    ',end='')

data.sort()
mf = (len(data)) //2
print(f'중앙값 : {data[mf]}    ',end='')

min = data[0]
for i in data :
    if min > i :
        min = i

max = data[1]
for i in data :
    if max < i :
        max = i
print(f'범위 : {max - min}',end='')