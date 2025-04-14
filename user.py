from book import Book
from libMgt import LibMgt

def userMenu():
    
    libMgt=LibMgt()

    ch=0
    while(ch!=6):
        print('''
                1. View Book 
                2. Book search By Id
                2. Book search By Name
                4. Issue Book
                5. Return Book
                6. Exit

        ''')
        ch=int(input("Enter Your Choice: "))
        if(ch==1):
            libMgt.showBook()

        elif(ch==2):
            id=int(input("Enter the id to search: "))
            libMgt.searchBookById(id)

        elif(ch==3):
            nm=input("Enter the Name to search: ")
            libMgt.searchBookByName(nm)        

        elif(ch==4):
            id=int(input("Enter the Book id: "))
            libMgt.issueBook(id)
        
        elif(ch==5):
            id=int(input("Enter the Book id: "))
            libMgt.returnBook(id)
        
        elif(ch==6):
            print("Thank you ")
