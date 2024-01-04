try:
    a=2+'2'
    print(a)
except TypeError:
    print('error handled')
finally:
    print('Excepton Handled')

def sum(a,b):
    return  a+b
print(sum(2,3))