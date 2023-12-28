import random
otp=''
while(True):
   otp=otp+str(random.randint(0,9))
   if len(otp)==4                                                                                                                        :
      break
print(' Hi Dear Your otp is ',otp)


