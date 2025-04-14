from admin import adminMenu
from user import userMenu 

if(__name__=="__main__"):

    print("***********************LIBRARY MANAGMENT***********************")

    print('''
        1. Admin Menu
        2. User Menu

      ''')

    ch=int(input("Enter Your choice: "))
    if(ch==1):
        username=input("Enter the Username: ")
        password=input("Enter the Password: ")
        if(username=="admin" and password=="admin123"):
            adminMenu()
        else:
            print("Wrong Crediential")   
    
    elif(ch==2):
        username=input("Enter the Username: ")
        password=input("Enter the Password: ")
        if(username=="user" and password=="user123"):
            userMenu()
        else:
            print("Wrong Crediential")     
