z = int(input())
array = []

for i in range (z):
    temp = input()
    array.append(temp)

for i in array:
    for j in range(0,len(i),2):
        print(i[j], end='')
    print(end=' ')
    for k in range(1,len(i),2):
        print(i[k], end='')
    print()
