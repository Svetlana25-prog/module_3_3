def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params()
print_params(a=10)
print_params(a=20, b='hello')
print_params(a=30, b=40, c=False)
print_params(a=30, c=50)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [10, 'hello', True]
values_dict = {'a': 1, 'b': 'строка', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [10, 'строка']

print_params(*values_list_2, 42)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)