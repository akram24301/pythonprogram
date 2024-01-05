def fun(a,b):
    for var in range(a,b+1):
        yield var**2
        yield var*2

out=fun(5,15)

print(list(out))