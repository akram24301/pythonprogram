def fact(a,n=1):
    if a==n:
        return n
    return n*fact(a,n+1)
out=fact(5)
print(out)
    
    
