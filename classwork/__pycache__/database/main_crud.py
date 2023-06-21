import connection
import pymysql
#connect with database

mydb=pymysql.connect(host="localhost",user="root",password="",database="14march_python")

mycursor=mydb.cursor()

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
        name=input("enter your name:")
        subject=input("enter your subject:")

        #query
        query="insert into students(name,subject)values('%s','%s')"

        args=(name,subject)

        mycursor.execute(query%args)

        #to save changes

        mydb.commit()

        print("successfully data inserted")
    elif choice==2:
        #to fetch all data from the table
        query="select * from students"

        #to execute the query
        mycursor.execute(query) 
        mydb.commit()

        #to fetch data from table
        data=mycursor.fetchall()
        print(data)
    elif choice==3:
        #update
        id=int(input("enter id:"))
        name=input("enter name:")
        subject=input("enter subject:")

        #query
        query="update students set name='%s',subject='%s' where id=%s"
        args=(name,subject,id)

        mycursor.execute(query%args)
        mydb.commit()
        print("data updated successfully")

    elif choice==4:
        #search data
        id=int(input("enter the id"))

        #query
        query="select * from students where id=%s"

        #args
        args=(id)

        mycursor.execute(query%args)

        #display all data in row variable

        row=mycursor.fetchone()

        #id=0 name=1 subject=2

        displayname=row[1]
        displaysubject=row[2]

        #print
        print("name=",displayname)
        print("subject=",displaysubject)

        mydb.commit()

    elif choice==5:
        #delete data
        id=int(input("enter your id:"))

        #query
        query="delete from students where id=%s"

        #args
        args=(id)

        mycursor.execute(query%args)
        mydb.commit()

        print("data deleted successfully")


        loop_choice=input("do you want to perform more operations? press 'y' for yes and 'n' for no")

        if loop_choice=='n' or loop_choice=='no':
            status=False