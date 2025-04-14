from book import Book
from libMgt import LibMgt

def adminMenu():

    libMgt=LibMgt()

    ch = 0
    while(ch!=10):
        print('''
                1. Add Book
                2. Show All Books
                3. Search Book By ID
                4. Search Book By Name
                5. Search Book By Author
                6. Edit Book By ID
                7. Edit Book By Name
                8. Delete Book by ID
                9. Delete Book by Name
                10. Exit
        
        ''')
        
        ch = int(input("Enter your choice: "))
        if(ch==1):
            bid=int(input("Enter id:"))
            bnm=input("Enter name: ")
            bath=input("Enter author name:")
            b=Book(bid,bnm,bath,status=1)
            libMgt.addBook(b)

        elif(ch==2):
            libMgt.showBook()
        
        elif(ch==3):
            id=int(input("Enter the id to search: "))
            libMgt.searchBookById(id)
        elif(ch==10):
            print("Thnak you")   

        elif(ch==4):
            nm=input("Enter the Name to search: ")
            libMgt.searchBookByname(nm)

        elif(ch==5):
            ath=input("Enter the Book Author Name to search: ")
            libMgt.searchBookByAuthor(ath)

        elif(ch==6):
            id=int(input("Enter the Book ID to Edit: "))
            libMgt.editBookById(id)

        elif(ch==7):
            nm=input("Enter the Book Name  to Edit: ")
            libMgt.editBookByName(nm)

        elif(ch==8):
            id=int(input("Delete the Book By ID: "))
            libMgt.deleteBookById(id) 

        elif(ch==9):
            nm=input("Delete the Book By Name: ")
            libMgt.deleteBookByName(nm)      

            
        

if(__name__=="__main__"):
        adminMenu()            