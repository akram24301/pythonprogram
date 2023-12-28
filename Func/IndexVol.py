def vol_index(a):
    lis=[]
    for i in range(0,len(a)):
        if a[i] in 'aeiouAEIOU':
            lis=lis+[i]
    return lis
c=vol_index('india')
print(c)

        
