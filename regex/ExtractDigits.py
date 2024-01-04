# import re
# st="The Date is 04/01/2024"
# data=re.findall('\d',st)
# print(data)#['0', '4', '0', '1', '2', '0', '2', '4']

#-----match two numbers at a time
# import re
# st="The Date is 04/01/2024"
# data=re.findall('\d{2}',st)
# print(data)

# #----to extract only even numbers
# import re
# st="The Date is 04/01/2024"

# data=re.findall('[24680]',st)
# print(data)     #['0', '4', '0', '2', '0', '2', '4']


# import re
# st="The Date 33 92 54 is 04/01/2024"
# data=re.findall('\d[24680]',st)
# print(data)  #['92', '54', '04', '20', '24']

#\d represent the first digit of the number
#[24680]matching second digit number






# import re
# st="1 6 567 The Date is 04/01/2024"

# data=re.findall('\d+',st)
# print(data)     #['1', '6', '567', '04', '01', '2024']

# #\d single digit if we want more one digit take '+'


#-------extract the pancard number
# import re
# st="CIKAP3684P  ICKPA7735P is your Pan number"

# data=re.findall('[A-Z]{5}\d{4}[A-Z]',st)
# print(data) #['CIKAP3684P', 'ICKPA7735P']


#-------extract the VEHICLE number up to 40

# import re
# st="AP40AK4556    KA42KT1256"

# data=re.findall('AP[0-3][0-9][A-Z]{2}[0-9]{4}|AP40[A-Z]{2}[0-9]{4}',st)
# print(data)


#=================to extract the mobile number
# import re
# st="+91-8526931478 +91-9526931478 +91-7526931478 +91-65246931478 +91-5526931478"

# data=re.findall('\+91-[6789][0-9]{9}',st)
# print(data)

#------------- extract email
import re
st="akram454ssh@gmail.com  bcbchc88b@gmail.in"

data=re.findall('[a-zA-Z]+[a-zA-Z0-9]*\@gmail*\.com',st)
print(data)
