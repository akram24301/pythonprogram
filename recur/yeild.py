def view(a):
    for i in range(0,len(a)):
        if type(a[i]) in [list,str,tuple,set,dict]:
            
            yield len(a[i])
        else: 
            yield a[i]
out=view([1,[4,5,6],{7,8},{'a':1},9.5,12])
print(list(out))