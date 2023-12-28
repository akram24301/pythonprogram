a=[-1,-23,3,-4,2]
out=a[0]
out2=a[0]
for i in a:
    if out<i:
        out2=out
        out=i
    elif out2<i:
        out2=i
print(out,out2)