# Функции. Задание 1
def get_summ(one, two, delimiter='&'):
    result = one + delimiter + two
    return result.upper()


summ = get_summ('Learn', 'python')
print(summ)
