calls = 0
def count_calls():
    global calls
    calls+=1
    return calls
def string_info(string):
    count_calls()
    d = len(string)
    string_up = string.upper()
    string_lo = string.lower()
    return d, string_up, string_lo

def is_contains(string, list1):
    count_calls()
    for world in list1:
        if world.lower() == string.lower():
            return True
        return False



print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)