a=[4,7,6,0,5,8,7]
'''i=1
sum=0
while i<len(a):
    sum+=a[i]
    i+=1
print(sum)'''

def add_int(var,i=0):
    if len(var)-1==i:
        if var[i]%2==0:
            return var[i]
        else: return 0
    if var[i]%2==0:
        return var[i]+add_int(var,i+1)
    else:
        return add_int(var,i+1)
out=add_int(a)
print(out)

