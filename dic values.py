d={}
while True:
    print(d)
    choice=int(input("1-reg, 2-login, 3:update , 4:delete user"))
    if choice==1:
            user=input("enter user name")
            pas=input ("enter password")
            if user in d.keys():
                   print("user exist")
            else:
                   d[user]=pas
                   
    if choice==2:
        user=input("enter user name")
        if user in d.keys():
            pas=input("enter password")
            if d[user]==pas:
                print("login successful")
            else:
                print("user name or password doesnot match")
        else:
            print("user doesnot exist please register")
            

    if choice==3:
        user= input("enter user name to update password")
        if user in d.keys():
            pas1=input("enter password to update")
            d[user]=pas1
            print("password updated successfully")
        else:
            print("user doesnot exist")

    
    if choice==4:
        user= input("enter user name to delete the user")
        if user in d.keys():
            del d[user]
            print("user deleted susccessfully")
        else:
            print("user doesnot exist")
