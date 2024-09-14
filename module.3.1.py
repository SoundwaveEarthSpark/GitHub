calls = 0
def count_calls() :
    global calls
    calls += 1

def  string_info(string):
    letters = len(string)
    high_string = string.upper()
    low_string = string.lower()
    count_calls()
    return letters, high_string, low_string



def is_contains(string, list_to_search):
    a = True
    for st in list_to_search:
        if string.upper() == st.upper():
            a = True
            break
        else:
            a = False
    count_calls()
    return a


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
