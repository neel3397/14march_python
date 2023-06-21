db={}
def registration(firstname,email,password):
    db["name"]=firstname
    db["email"]=email
    db["password"]=password
    print("registration successfully!")
def login(email,password):
    if email==db["email"]:
       if password==db["password"]:
           return db["name"]
       else:
           return print("inavlid or password")
    else:
        return print("invalid email or password")
status=True
while status:
        menu="""
            1-press 1 for registration
            2-press 2 for login
            3-press 3 for exit
        """
        print(menu)
        choice=int(input("enter your choice"))
        if choice==1:
            name=input("enter your name:")
            email=input("enter your email:")
            password=input("enter your password:")
            registration(name,email,password)

        elif choice==2:
            email=input("enter your email")
            password=input("enter your password")
            login(email,password)

        elif choice==3:
            print("thank you for using our application")
            status=False