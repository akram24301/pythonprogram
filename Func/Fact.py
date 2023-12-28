def fact(num):
    f=1
    i=1
    while num!=0:
        f=f*i
        i+=1
        num-=1
    return f
factorial=fact(5)
print(                                                                                                          factorial)