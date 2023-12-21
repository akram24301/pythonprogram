a='hello'
vol=0
cons=0
for var in a:
    if  'A'<= var <='Z' or 'a'<=var <='z' :
       if var in 'aeiouAEIOU':
            vol=vol+1
       else:
           cons=cons+1
        
print('vowels :',vol)
print('consonants :',cons)
