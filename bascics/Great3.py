num1=int(input('Enter the num1: '))
num2=int(input('Enter the  num2: '))
num3=int(input('Enter the  num3: '))
if  num1>num2 and num1>num3:
    print(num1,'is greatest than',num2,num3)
elif num2>num3:
    print(num2,' is greatest than ',num1,num3)
else:
    print(num3,'is the greatest than',num1,num2)