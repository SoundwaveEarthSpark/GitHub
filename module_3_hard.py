def list_count(element):
    sum_element = 0
    for i in element:
        if type(i) == str:
            sum_element= sum_element + len(i)
        elif type(i) == int or type(i) == float:
            sum_element = sum_element + i
        else:
            sum_element += calculate_structure_sum(i)
    return sum_element

def dict_count(element):
    sum_dict = 0
    dict_keys = element.keys()
    sum_dict_keys = 0
    for i in dict_keys:
        sum_dict_keys = sum_dict_keys + len(i)
    for v in element.values():
        if isinstance(v, (int, float)):
            sum_dict += v
        else:
            sum_dict += calculate_structure_sum(v)
    sum_dict = sum_dict + sum_dict_keys
    return sum_dict



def calculate_structure_sum(*args):
    result = 0
    for element in args:
        element_type = type(element)
        if element_type == list:
            result += list_count(element)
        elif element_type == dict:
            result += dict_count(element)
        elif element_type == tuple:
            result += list_count(element)
        elif element_type == set:
            result += list_count(list(element))
        elif element_type == str:
            result += len(element)
        elif element_type == int or element_type == float:
            result += element
        else:
            continue
    return result

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

