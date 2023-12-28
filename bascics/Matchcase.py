seats=int(input('Enter the seats :'))
option=int(input(('Enter the option')))
match option:
    case 1:
        print("Diamond class")
        amt=seats*200
    case 2:
        print("Gold class")
        amt=seats*150
    case 3:
        print("Silver Class")
        amt=seats*100
print(amt)