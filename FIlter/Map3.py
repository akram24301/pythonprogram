def data_iterator(a):
    if a%2==1:
        return True
    else:
        return False
def square(b):
    return b**2
out=map(square,(filter(data_iterator,range(1,101))))
print(list(out))