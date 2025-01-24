def concatenate_values_with_commas_and_insert_and_before_the_last_value(list):
    FIRST = 0
    LAST = len(list) - 1

    for i in range(len(list)):
        elem = str(list[i])

        if i == FIRST:
            s = elem
        elif i == LAST:
            s += ' and ' + elem
        else:
            s += ', ' + elem

    return s


spam = ['apples', 'bananas', 'tofu', 'cats']
s = concatenate_values_with_commas_and_insert_and_before_the_last_value(spam)
print(s)
