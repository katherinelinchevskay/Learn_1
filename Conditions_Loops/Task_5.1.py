#  Write a code with all types of loops: Array with any data and loop that can handle it.

numbers = [0, 10, 20, 30, 40, 5, 6, 7]
for i in range(len(numbers)):
    print(numbers[i])

j = int(input())
while j in numbers:
    print('Yes')
    j += 1
