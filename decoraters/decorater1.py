def add(a,b):
    return a+b

def cal(func):
    def inner():
        print('operation started')
        func()
        print('operation done')
    return inner

@cal #add=cal(add)
def add():
    a=int(input('enter a :-'))
    b=int(input('enter b :-'))
    print(a+b)
add()
        