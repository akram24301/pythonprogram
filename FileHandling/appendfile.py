file=open("mca.txt",'a')
data=" \n get ready for internals." 
file.write(data)
file.close()

file=open('mca.txt','r')
data=file.read()
print(data)
file.close()