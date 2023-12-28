a=str(input('Enter the word :'))
count=0
i=0
while i<len(a):
    if a[i] in 'AEIOUaeiou':
        count=count+1
    i+=1

print(count) 