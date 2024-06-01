# def my_func():
#     my_var = 'some text'
#     print(my_var)
# print(my_var) Вызов переменной не произойдет т.к. переменная 
# my_var является локальной и мы не можем обратиться к ней в не функции
# my_func()



# var1 = 5
# var2 = 10 

# def my_func():
#     var = 15
#     print(var1)
#     print(var2)
# переменные var1 var2 голобальные поэтому к ним 
# можно обрашаться в нутри функции

# my_func()

# var область видимости
# var = 1 

# def fnc1():
#     # локальная область видимости
#     print(var + 2)

# def fnc2():
#     # локальная область видимости
#     print(var + 5)

# fnc1()
# fnc2() 

# a = 1
# def fnc():
    # b=5
# b локальная переменная
# a глобальная переменная
# fnc()

# a = 1 
# def fnc1():
#     b = 2 

#     def fnc2():
#         c = 3 
#         print(a)
#         print(b)
#         print(c)
        
#     fnc2()

# fnc1()
    
# a = 1 
# def fnc1():
#     a = 2 
#     print(a)

# fnc1()

