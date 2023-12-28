def data_iterator(a):
    if 'a'<=a <='z':
        return True
    else:
        return False
def ascii(b):
    return ord(b)

out=map(ascii,filter(data_iterator,'a1b2c3Def12@#9'))
print(list(out))

c=map(lambda d:ord(d),filter(lambda a:'a'<= a <='z','a1b2c3Def12@#9'))
print(list(c))