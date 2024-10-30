def personal_sum(numbers):
    results = 0
    incorrect_data = 0
    for n in numbers:
        try:
            results += n
        except TypeError:
            print(f"Некорректный тип данных для подсчёта суммы - {n}")
            incorrect_data += 1
    return results, incorrect_data

def calculate_average(numbers):
    try:
        n_sum, count = personal_sum(numbers)
        result =  n_sum / (len(numbers) - count)
        return result
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать