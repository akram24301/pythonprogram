num=int(input('Enter the number :.....'))
i=2
temp=False
while i<=num:
    if num%i==0 :
        temp=True
    i=i+1
if not temp:
    print(num,' is a prime ')
else:
    print(num,'not a prime')