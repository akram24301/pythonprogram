class base:
    a=10
    b=20
    def __init__(self,c):
        self.c=c
    
class derived(base):
    def __init__(self, c,e,d):
        base.__init__(self,c)
        self.e=e
        self.d=d

obj=derived(6,56,58)