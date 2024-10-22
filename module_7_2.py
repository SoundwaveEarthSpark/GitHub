def custom_write(file_name, strings):
    strings_positions = {}
    number = 0
    key = ''
    bite = 0
    file = open(file_name, 'w', encoding="utf-8")
    for i in strings:
        number += 1
        bite = file.tell()
        file.write(str(f'\n{i}'))
        key =f'({number}:{bite})'
        strings_positions[key] = i
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
