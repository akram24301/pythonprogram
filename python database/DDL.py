import pymysql
con=pymysql.connect(user='root',password='root',port=3306,database='pythonmysql')
cursor=con.cursor()
def create_table():
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

                #-----to insert records
def insert_record():
    query='''insert into customer(id,name,mobile,balance)
    values(1,'Akram',9676558844,25000)'''
    cursor.execute(query)
    con.commit()
#insert_record()
                #-----to  fectch records
def get_records():
    query="select * from customer"
    cursor.execute(query)
    records=cursor.fetchall()
    for i in records:
        print(i)
#get_records()
    
                #-------to insert records dynamically
def insert_dynamic(cid,name,mobile,bal):

    record=(cid,name,mobile,bal)
    query="insert into customer(id,name,mobile,balance) values(%s,%s,%s,%s)"
    cursor.execute(query,record)
    con.commit() #call the function in interactive mode


                #-------to drop a record dynamically
def drop_record(cid):
    query=f'delete from customer where id={cid}'
    cursor.execute(query)
    con.commit()
    print('record removed')

                #------to update a record dynamically
    
def update_name(cid,newvalue):
    query='update customer set name = %s where id=%s'
    print(query)
    cursor.execute(query,(newvalue,cid))
    con.commit()
    print('record updated')

  
