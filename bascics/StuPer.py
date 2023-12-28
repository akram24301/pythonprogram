m=eval(input('Enter the marks : '))
if m>=90 and m<=100:
    print('A+ : Grade')
elif m>=80 and m<90:
    print('A : Grade')
elif m>=70 and m<80:
    print('B : Grade')
elif m>=60 and m<70:
    print('C :Grade')
elif m>=35 and m<60:
    print('D : Grade')
elif m>=0 and m<35:
    print('Fail')
else:
    print('Enter the valid marks')
