mes_c = int(input())
for mes in range(6):
    if mes_c > 6:
        print('You have ' + str(mes_c) + ' new messaage')
    elif mes_c == 0:
        print('You don`t have new message')
    else:
        print('you have less then 6 message')
