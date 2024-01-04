# import re
# with open(r"C:\Users\Administrator.MCA\Desktop\hello python.txt",'r')as file:

#    data=file.read()
#    data1=re.split(' ',data)
#    count=0
#    words=[]
#    for i in data1:
#       out=re.match('^a',i)
#       if out:
#          words+=[i]
#          count+=1
#    print(count)
#    print(words)

import re
with open(r"C:\Users\Administrator.MCA\Desktop\hello python.txt",'r+')as file:

   data=file.read()
   data1=re.sub('a','@',data)
   file.write(data1)
   
