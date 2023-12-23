import random
num=random.randint(1,10)
while(True):
    a=int(input('Enter the number : '))
    if a==num:
        print('congrats you sucessfully gussed the number',num)
        break
    elif a<num:
        print('Enter greater Number')
    elif a>num:
        print('Enter the lesser number')