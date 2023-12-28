a=input('enter the operation ')
op1=int(input('enter op 1'))
op2=int(input('enter op 2'))
match a:
    case '+':
        print(op1+op2)
    case '-':
        print(op1-op2)
    case '*':
        print(op1*op2)
    case '/':
        print(op1/op2)
    case _:
        print('invalid operation')