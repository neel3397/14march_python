import pymysql

mysf=pymysql.connect(host="localhost",user="root",password="")

mycursor=mysf.cursor()

#execute the query
mycursor.execute("create database if not exists neel")

#save
mysf.commit()
print("database succesfully created")


#db connection
mysf=pymysql.connect(host="localhost",user="root",password="",database="neel")

mycursor=mysf.cursor()

#table creation query executation

mycursor.execute("create table if not exists students(id int primary key auto_increment,name varchar(50),subject varchar(50))")
mysf.commit()
print("table created successfully!")

