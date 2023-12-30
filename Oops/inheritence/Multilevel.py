class grand:
    
    def __init__(self,a,b):
        self.a=a
        self.b=b

class parent(grand):
    
    def __init__(self,a,b,c,d):
        super.__init__(self,a,b)
        self.c=c
        self.d=d
    
class derived(parent):
    def __init__(self, a,b,c,d,e,f):
        super.__init__(self,a,b,c,d)
        self.e=e
        self.f=f

obj=derived(20,30,40,50,60,70)