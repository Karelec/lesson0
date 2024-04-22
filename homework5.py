my_list = ["Green", "Red", "Blue", "Orange", "Brown"]
print(my_list)
print('Первый элемент: ', my_list[0])
print('Последний элемент: ', my_list[-1])
my_list[2] = "Yellow"
print(my_list)
my_dict = {'RJ-45': 8, 'RJ-11': 4, 'COM': 9, 'VGA': 15}
print(my_dict)
print('Для гигабитного канала используем',my_dict['RJ-45'], 'пинов')
my_dict['RJ-45'] = 4
print('Для канала 100 мб используем', my_dict['RJ-45'], 'пина')