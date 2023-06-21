import pymysql

mydb=pymysql.connect(host="localhost",user="root",password="")

mycursor=mydb.cursor()

#execute the query
mycursor.execute("create database if not exists 14march_python")

#save
mydb.commit()
print("database succesfully created")


#db connection
mydb=pymysql.connect(host="localhost",user="root",password="",database="14march_python")

mycursor=mydb.cursor()

#table creation query executation

mycursor.execute("create table if not exists students(id int primary key auto_increment,name varchar(50),subject varchar(50))")
mydb.commit()
print("table created successfully!")

