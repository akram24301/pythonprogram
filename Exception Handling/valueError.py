try:
    a=dict('34')
    print(a)
except TypeError:
    print('error handled')
except ValueError:
    print('cannot type cast string to dict')
finally:
    print('Excepton Handled')


def sum(a,b):
    return  a+b
print(sum(2,3))