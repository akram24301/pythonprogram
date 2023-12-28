a=[1,2,3]
b=[4,4,4]
c=[1,5,5]
lis=[]
for i,j,k in zip(a,b,c):
    lis=lis+[i]+[j]+[k]
print(lis)