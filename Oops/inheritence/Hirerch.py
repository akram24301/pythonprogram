class car:
    name="Cars"

    def __init__(self,name,mileage,price,color):
        self.name=name
        self.mileage=mileage
        self.price=price
        self.color=color

class supra(car):
    pass

class bmw(car):
    pass

c1=supra("supra mk4",10,50000,"black")
c2=bmw("bmw m4",15,5000000,"white")
    