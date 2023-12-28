def double(a):
    if a%2==0:
        return a*2
    else :
        return a**3
a=map(double,[1,2,3,4])
print(list(a))