for current_hour in range(24):
    if current_hour < 12:
        print('Good morning')
    elif current_hour  == 12:
        print('Good afternoon')
    else:
        print('Good evening')