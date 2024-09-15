def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print('Функция с параметрами по умолчанию:')
print_params()
print_params(a=7)
print_params(b=25)
print_params(c=[1, 2, 3])
print()

print("Распаковка параметров:")
values_list =[1, 'line', False]
values_dict = {'a': 5, 'b': 'hop', 'c': False}

print_params(*values_list)
print_params(**values_dict)
print()

print('Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)