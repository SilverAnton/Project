def calc_add(num, symbol):
    '''функция прибавляет к числу 10, нужно выбрать число и знак +, в качестве аргументов'''
    if symbol == '+':
        num_add = num + 10
        return num_add
    else:
        print('ой')


def calc_subst(num, symbol):
    '''функция отнимает от числа 10, нужно выбрать число и знак -, в качестве аргументов'''
    if symbol == '-':
        num_subst = num - 10
        return num_subst
    else:
        print('ой')


item = calc_add(50, '+')
print(item)