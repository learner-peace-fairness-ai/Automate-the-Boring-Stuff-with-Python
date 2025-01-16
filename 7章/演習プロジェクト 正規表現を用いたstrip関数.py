import re

def strip_by_regular_expression(s, chars=None):
    if chars:
        tgt = chars
    else:
        tgt = r'\s'

    head_target_regex = re.compile(f'^[{tgt}]+')
    result = head_target_regex.sub('', s)
    
    tail_target_regex = re.compile(f'[{tgt}]+$')
    result = tail_target_regex.sub('', result)
    
    return result


s1 = strip_by_regular_expression('aaa')
print(s1, len(s1))

s2 = strip_by_regular_expression('   bbb   ')
print(s2, len(s2))

s3 = strip_by_regular_expression('ABC111CBA', 'ABC')
print(s3, len(s3))

s4 = strip_by_regular_expression('ABC111ABC222CBA', 'ABC')
print(s4, len(s4))