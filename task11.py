print('1-st floor')
print('Enter number of floor')
b = int(input())
for i in range(2, b+1,1):
    if i != b:
        print('Current floor is ',  i, 'next floor is ',  i + 1)
    else:
        print('Current floor is ', b)