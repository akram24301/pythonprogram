try:
    a=2+'2'
    print(a)
    b=dict('34')
    print(b)
except (TypeError,ValueError):
    print('error handled type error,value error cannot type cast string to dict')
finally:
    print('Excepton Handled')

def sum(a,b):
    return  a+b
print(sum(2,3))
