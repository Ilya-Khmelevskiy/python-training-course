def print_menu(printing_menu):
    for dish in printing_menu:
        print(dish)
    print('\n')


dishes_list = ['fish', 'meat', 'ice cream', 'french frees', 'cheese']
menu = tuple(dishes_list)

print_menu(menu)

try:
    menu[0] = 'bread'
except TypeError:
    print('Error message\n')

dishes_list[-1] = 'bread'
menu = tuple(dishes_list)
print_menu(menu)

