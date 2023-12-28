import random
cap=''
while len(cap)<6:
    cap=cap+chr(random.randrange(65,90))
    cap=cap+chr(random.randrange(97,122))
    cap=cap+str(random.randrange(0,9))
print(cap)