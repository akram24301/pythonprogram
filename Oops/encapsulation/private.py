class sample:
    __a=30
    b=40

    def __init__(self,c,d):
        self._c=c
        self.d=d
    def __update_c(self,new):
        self.c=new
    def display(self):
        print(self.__a,self._c)
class child(sample):
    pass