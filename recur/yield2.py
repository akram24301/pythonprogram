def cal(a,b):
    yield a+b
    yield a-b
    yield a*b
out=cal(10,5)
print(out)