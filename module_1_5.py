immutable_var = (9, 6,"legend",[1, 3])
print(immutable_var)

#immutable_var[0] = 4
#print(immutable_var)
#приведенные выше команды не сработают, ведь кортеж неизменяем
#ОДНАКО можно изменить значения в элементе списка в кортеже
immutable_var[3][1] = 1
print(immutable_var)

mutable_list = [1, 3, 5, 6, 3, 'Seven', ]
print(mutable_list)
mutable_list[0] = 6
print(mutable_list)