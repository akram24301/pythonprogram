from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self,name,color,price):
            self.name=name
            self.color=color
            self.price=price
            self.speed=0
    @abstractmethod
    def stop():
         pass
    @abstractmethod
    def speedup():
         pass
    
class BMW(car):
    def speedup(self):
        self.speed+=5
        return self.speed
    def stop(self):
        self.speed=0

class TATA(car):
    def speedup(self):
        self.speed+=5
    def stop(self):
        self.speed=0
        return self.speed
BMW1=BMW('x7','black',2000)
neon=TATA('neon1','white',1000)
    
