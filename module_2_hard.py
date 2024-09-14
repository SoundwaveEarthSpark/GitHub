n = int(input('Введите число:'))
result = []
for i in range(1, 20):
    for j in range(i, n):
        if n % (j + i) == 0 and i != j:
            result.append(i)
            result.append(j)
            continue
        else:
            continue
print(*result, sep='')
