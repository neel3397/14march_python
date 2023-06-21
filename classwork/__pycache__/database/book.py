import connection
import pymysql
#connect with database

mybook=pymysql.connect(host="localhost",user="root",password="",database="book")

mycursor=mybook.cursor()

status=True
while status:
    menu="""
            1-insert data
            2-view data
            3-update data
            4-search data
            5-delete data
        """
        
    print(menu)

    choice=int(input("enter your choice:"))

    if choice==1:
        #to insert data
        #id ,name ,isbn no. ,price
        name=input("enter your name:")
        isbnnumber=input("enter your isbnnumber:")
        price=input("enter your price")

        #query
        query="insert into students(name,isbnnumber,price)values('%s','%s','%s')"

        args=(name,isbnnumber,price)

        mycursor.execute(query%args)

        #to save changes

        mybook.commit()

        print("successfully data inserted")
    elif choice==2:
        #to fetch all data from the table
        query="select * from mybook"

        #to execute the query
        mycursor.execute(query) 
        mybook.commit()

        #to fetch data from table
        data=mycursor.fetchall()
        print(data)


        loop_choice=input("do you want to perform more operations? press 'y' for yes and 'n' for no")

        if loop_choice=='n' or loop_choice=='no':
            status=False