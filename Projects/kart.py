class Kart:
    quantity={'tv':10,'mobile':20,'laptop':5}
    price ={'tv':10000,'mobile':5000,'laptop':20000}

    def __init__(self,name,mob,loc):
        self.name        = name
        self.mob         = mob
        self.loc         = loc
        self.product_qty = 0
        self.total_price = 0 

    @classmethod
    def __modify_class(cls,product,qty):
        cls.quantity[product]-=qty

    @classmethod
    def available_product(cls):
        print(cls.quantity)

    def get_bill(self):
        custid=self.name[0:4]+str(self.mob)[-:] 
        data = f'''
                custid:-{custid}
                name :- {self.name}
                mobile:-{self.mob}
                location:-{self.loc}
                total quantity booked :- {self.product_qty}
                total price           :-{self.total_price}

                Thank you for using My kart!!!

                
            '''
        with open(f'{custid}.txt','w') as file:
            file.write(data)
        
    def book_product(self):
        pro_count=0
        total_price=0
        while True:
            self.available_product()
            product=input("enter \n1 for tv,\n2 for mobile\n3 for laptop :-  ")
            qty = int(input('enter quantity :- '))
            pro_count+=qty
            if product=='1':
                price=self.price['tv'] *qty
                total_price+=price
                print(f'product {qty} Tv with total price {price}')
                self.__modify_class('tv',qty)
            elif product=='2':
                price=self.price['mobile'] *qty
                total_price+=price
                print(f'product {qty} mobile with total price {price}')
                self.__modify_class('mobile',qty)
            elif product=='3':
                price=self.price['laptop'] *qty
                total_price+=price
                print(f'product {qty} laptop with total price {price}')
                self.__modify_class('laptop',qty)
            

            print('Wish to book another product!' )
            response = input('press YES/Y/y or press any key ')
            if response in['YES','Y','yes','y']:
                continue
            else:
                print('Thank you for using my kart')
                break
        if  pro_count and total_price:
                self.product_qty+=pro_count
                self.total_price+=total_price


        