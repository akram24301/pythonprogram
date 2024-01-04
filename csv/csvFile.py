import csv
#------> To write a file
# with open('mca.csv','w',newline='') as csvfile:
#     data=csv.writer(csvfile)
#     data.writerow(['id','name','mobile','email'])
#     data2=[
#         [1,'john',5454544454,'john@123'],
#         [2,'rolex',4454454,'akespeare@gmail.com'],
#         [3,'yahoo',4454454,'s@gmail.com'],
#     ]
#     data.writerows(data2)


# ------->to read a csv file

# with open('mca.csv','r') as csvfile:
#     data=csv.reader(csvfile)
#     for i in data:
#         print(i)


#csv file usinng dictionary DictWriter()

# with open('mca1.csv','w',newline='') as csvfile:
#     fieldnames = ['id','name','mobile','email']
#     data = csv.DictWriter(csvfile,fieldnames)
#     data.writeheader()
#     rows=[
#         {'id':1,'name':'Akram','mobile':861776445,'email':'akram@gmail.com'},

#         {'name':'Sameer','id':2,'email':'sameer@gmail.com','mobile':967668623},

#     ]
#     data.writerows(rows)

# csv file read using DictReader

with open('mca1.csv','r') as csvfile:

    data=csv.DictReader(csvfile)
    for row in data:
        print(row['name'])
        print(row)