
#----------------example of call back fun

def add(a,b):
    return a+b
def sub(a,b):
    return a-b;
def mul(a,b):
    return a*b
def cal(fun,a,b):
    return fun(a,b)
print(cal(mul,4,5))
print(cal(add,4,6))
print(cal(sub,10,6))