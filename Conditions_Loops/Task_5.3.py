loop = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
index = 0
for i in loop:
    if i % 2 == 0:
        odd.append((index, i))
    else:
        even.append((index, i))
    index += 1

print(f'{odd}\n{even}')
