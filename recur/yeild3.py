

def fun(b):
    for i in range(0,len(b)):
        if b[i] in 'aeiouAEIOU':
            yield b[i]
            yield i
out=fun("God father anil")
res=''
for i in out:
    res+=str(i)
print(res)

        