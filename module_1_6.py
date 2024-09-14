my_dict = {'Pen': 2, 'Pencil': 1, 'Brush': 3}
print('Dict:', my_dict)
print('Existing value:',my_dict['Pen'])
print('Not existing value:', my_dict.get('Liner'))
my_dict.update({'Liner': 5, 'Paint': 7})
a = my_dict.pop('Pencil')
print('Not existing value:', a)
print('Modified dictionary:', my_dict)

#Множества

my_set={1, 4, 4, 'Hi!', True, 3, 'Hi!'}
print('Set:', my_set)
my_set.update({'Bye!', 42.123})
my_set.discard(4)
print('Modified set:', my_set)

