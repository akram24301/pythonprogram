num=input('Enter the Binary Numbers :')
i=0
con=''
while i<len(num):
    if num[i]=='0':
        con=con+'1'
    else:
        con=con+'0'
    i+=1
print(con)
