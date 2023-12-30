class  add:
    @staticmethod
    def add(a,b):
        return a+b
class sub:
    @staticmethod
    def sub(a,b):
        return a-b
class cal(add,sub):
    pass

obj=cal()
obj.add(5,3)
obj.sub(10,5)