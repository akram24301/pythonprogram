def fname(a):
    if a%2==0:
        return  True
    else:
        return False
out=filter(fname,[2,5,6,54,5,6,5,])
print(list(out))