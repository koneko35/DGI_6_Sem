# zadanie 1
def change_string(str):
    str = 'РТ1, ' + str
    print('Значение строки после изменения значения =', str)
    print('Id строки после изменения значения =', id(str))
    print('\n')

my_str = 'привет!'
print('Значение строки до вызова функции =', my_str)
print('Id строки до вызова функции =', id(my_str))
print('\n')

change_string(my_str)
print('Значение строки после вызова функции =', my_str)
print('Id строки после вызова функции =', id(my_str))
print('\n')


# zadanie 2

def change_list(list):
    list.append('привет!')
    print('Значение списка после изменения значения =', list)
    print('Id списка после изменения значения =', id(list))
    print('\n')

my_list =['РТ1,']
print('Значение списка до вызова функции =', my_list)
print('Id списка до вызова функции =', id(my_list))
print('\n')

change_list(my_list)
print('Значение списка после вызова функции =', my_list)
print('Id списка после вызова функции =', id(my_list))
print('\n')

# zadanie 3

# zadanie 4

def change_list(list):
    list[0][0]=4
    print('Значение списка после изменения значения =', list)
    print('Id списка после изменения значения =', id(list))
    print('\n')

base_list=[1,2,3]
my_list = [base_list]*3
print('Значение списка до вызова функции =', my_list)
print('Id списка до вызова функции =', id(my_list))
print('\n')

change_list(my_list)
print('Значение списка после вызова функции =', my_list)
print('Id списка после вызова функции =', id(my_list))
print('\n')
