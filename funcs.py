def calc(num, symbol):
    if symbol == '+':
        num_add = num + 10
        return num_add
    #elif symbol == '-':
        #num_subst = num - 10
        #return num_subst
    else:
        print('ой')


item = calc(50, '+')
print(item)