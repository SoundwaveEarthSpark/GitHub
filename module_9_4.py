from random import choice

#lambda

first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))

#замыкание

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding="UTF-8") as file:
            file.writelines(f"{item}\n" for item in data_set)
            file.writelines('\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

#Метод __call__

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())