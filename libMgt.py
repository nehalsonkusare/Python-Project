from book import Book
from os import path
from datetime import datetime
class LibMgt:

    def addBook(self,b):
        fp=open("BookInfo.txt","a")
        fp.write(str(b))
        fp.write("\n")
        fp.close()

    def showBook(self):
        try:
            fp=open("Bookinfo.txt","r")
        except:
            print("File does not exist")
        else:
            data=fp.read()
            fp.close
            print(data)

    def searchBookById(self,id):
            if(path.exists("Bookinfo.txt")):
                with open("Bookinfo.txt","r") as fp:
                    Flag=False
                    for line in fp:
                        data=line.split(",")
                        if(data[0]==str(id)):
                            print("Book found...",line.strip())
                            Flag=True
                            break
                if(Flag==False):
                    print("Book not found")        
            else:
                print("File does not exist")

    def searchBookByname(self,name):
            if(path.exists("Bookinfo.txt")):
                with open("Bookinfo.txt","r") as fp:
                    Flag=False
                    for line in fp:
                        data=line.split(",")
                        if(data[1]==name):
                            print("Book found...",line)
                            Flag=True
                            break
                if(Flag==False):
                    print("Book not found")        
            else:
                print("File does not exist")  

    def searchBookByAuthor(self,author):
            if(path.exists("Bookinfo.txt")):
                with open("Bookinfo.txt","r") as fp:
                    Flag=False
                    for line in fp:
                        data=line.split(",")
                        if(data[2]==author):
                            print("Book found...",line)
                            Flag=True
                            break
                if(Flag==False):
                    print("Book not found")        
            else:
                print("File does not exist")                              

    def editBookById(self,id):
            Booklist=[]
            flag=False
            if(path.exists("Bookinfo.txt")):
                with open("Bookinfo.txt", "r") as fp:
                   for line in fp:
                        data=line.split(",")
                        if(data[0]==str(id)):
                            print("Record found",line.strip())
                            flag=True
                            ans=input("Do you want to cahnge Book name?(y/n): ")
                            if(ans.lower()=='y'):
                                data[1]=input("Enter the new Book name: ")
                                data[2]=input("Enter the Author name: ")
                            line=','.join(data)
                            line+='\n'
                        Booklist.append(line)
                if(flag==True):
                    with open("Bookinfo.txt", "w") as fp:
                        for book in Booklist:
                            fp.write(book)
                else:
                    print("Record not found")                        
            else:
                print("File does not exist")                        


    def editBookByName(self,name):
            Booklist=[]
            flag=False
            if(path.exists("Bookinfo.txt")):
                with open("Bookinfo.txt",'r') as fp:
                    for line in fp:
                        data=line.split(',')
                        if(data[1]==name):
                            print("Record found",line.strip())
                            flag=True
                            ans=input("Do you want to edit Book name?(y/n): ")
                            if(ans.lower()=='y'):
                                data[1]=input("Enter the new Book Name: ")
                                data[2]=input("Enter the Book Author Name: ")
                            line=','.join(data)
                            line+='\n'
                        Booklist.append(line)             
                if(flag==True):
                    with open("Bookinfo.txt",'w') as fp:
                        for book in Booklist:
                            fp.write(book)
                else:
                    print("Record not found")            
            else:
                print("File does not exist")    

    def deleteBookById(self,id):
        Booklist=[]
        flag=False
        if(path.exists("Bookinfo.txt")):
            with open("Bookinfo.txt","r") as fp:
                for line in fp:
                    data=line.split(",")
                    if(data[0]==str(id)):
                        flag=True
                        print("Record found.",line.strip())
                    else:
                        Booklist.append(line)

            if(flag==True):
                with open("Bookinfo.txt","w") as fp:
                    for book in Booklist:
                        fp.write(book)                  
        else:
            print("File does not exist")


    def deleteBookByName(self,name):
        Booklist=[]
        flag=False
        if(path.exists("Bookinfo.txt")):
            with open("Bookinfo.txt","r") as fp:
                for line in fp:
                    data=line.split(",")
                    if(data[1]==name):
                        flag=True
                        print("Record found.",line.strip())
                    else:
                        Booklist.append(line)
            if(flag==True):
                with open("Bookinfo.txt","w") as fp:
                    for book in Booklist:
                        fp.write(book)                   
        else:
            print("File does not exist.")


    def issueBook(self,id):
        Booklist=[]
        flag=False
        with open("Bookinfo.txt","r") as fp:
                for line in fp:
                    data=line.split(",")
                    if(data[0]==str(id)):
                    
                        print("Book Found: ",line.strip())
                        if(int(data[3])==1):
                            name=input("Enter the name of Borrower: ")
                            dateOfIssue=input("Enter the date of the issue(dd/mm/yyyy): ")
                            book=str(id)+","+name+","+dateOfIssue
                            print("Book issued successfully to",name)
                            with open("IssueBookInfo.txt","a") as fp1:
                                fp1.write(book)
                                fp1.write("\n")            
                                flag=True
                            data[3]="0\n"
                    
                        else:
                            print("Book is already issued.")
                    line=",".join(data)
                    Booklist.append(line)

        if(flag==True):
            with open("Bookinfo.txt","w") as fp:
                for book in Booklist:
                    fp.write(book)        
                  
        else:
            print("File does not exist")


    def returnBook(self,id):
        Booklist=[]
        flag=False
        with open("IssueBookInfo.txt","r") as fp:
            for line in fp:
                data=line.split(",")
                if(data[0]==str(id)):
                    print("Book found ")
                    dateOfIssue = data[2]
                    dateOfIssue = dateOfIssue.split("/")                    
                    dateOfSubmit=input("Enter the date of the submit(dd/mm/yyyy): ")
                    dateOfIssue = datetime(int(dateOfIssue[2]),int(dateOfIssue[1]),int(dateOfIssue[0]))
                    dateOfSubmit = dateOfSubmit.split("/")
                    dateOfSubmit = datetime(int(dateOfSubmit[2]),int(dateOfSubmit[1]),int(dateOfSubmit[0]))
                    days = (dateOfSubmit - dateOfIssue).days
                    if(days > 5):
                        fine = (days-5)*20
                        print("Please pay Rs."+str(fine)+"\-")
                    else:
                        print("No fine applicaple")

                    flag = True                    
                else:
                    Booklist.append(data)
            

            if(flag):                
                with open("IssueBookInfo.txt","w") as fp:
                    for book in Booklist:
                        book = ",".join(book)
                        fp.write(book)
                
                bookData = []
                with open("BookInfo.txt","r") as fp:
                    for line in fp:
                        if(str(id) in line):
                            line = line.split(",")
                            line[3] = "1\n"
                            line = ",".join(line)
                        bookData.append(line)

                with open("BookInfo.txt","w") as fp:
                    for book in bookData:
                        fp.write(book)



                
                    




            
