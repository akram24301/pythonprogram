import pymysql
con=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=con.cursor()
try:
    query='''
    create table customer(
    id int primary key,
    name varchar(100),
    mobile bigint unique,
    balance bigint
    );    
    '''
    cursor.execute(query)
except pymysql.err.OperationalError as e:
    print(f'{e}')