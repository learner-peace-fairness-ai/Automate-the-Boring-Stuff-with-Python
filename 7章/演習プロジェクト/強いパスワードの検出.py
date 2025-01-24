import re


def is_strong_password(s):
    more_than_8characters_regex = re.compile(r'.{8,}')
    if more_than_8characters_regex.search(s) is None:
        return False
    
    contains_uppercase_regex = re.compile(r'[A-Z]')
    if contains_uppercase_regex.search(s) is None:
        return False
    
    contains_lowercase_regex = re.compile(r'[a-z]')
    if contains_lowercase_regex.search(s) is None:
        return False

    contains_number_regex = re.compile(r'\d')
    if contains_number_regex.search(s) is None:
        return False
    
    return True


print(is_strong_password('1'))
print(is_strong_password('a'))
print(is_strong_password('abcdefgh'))
print(is_strong_password('ABCDEFGH'))
print(is_strong_password('ABCDefgh'))
print(is_strong_password('ABCDefg1'))
