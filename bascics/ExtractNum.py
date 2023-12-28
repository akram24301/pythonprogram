a=(input('Enter the Some thing........'))
con=''
i=1
while i<len(a):
    if '0'<=a[i]<='9':
        con=con+a[i]
    i=i+1

print(con)