print('Welcome to "Book My Show"')

name=input("Enter your Name : ")
seats=int(input("Enter the Number of Seats, you want to Book :"))
category=int(input('Please select \n 1.Diamond \n 2.Gold \n 3.Silver \n'))
if category==1:
       amount=seats*200
elif category==2:
    amount=seats*150
elif category==3:
    amount=seats*100
print(f'hi {name}you have booked {seats} seats and total amount is {amount}')