'''
Mainfile module
This module is the main module where all the other modules will be imported
and the main function of those modules will be called here so we can perform
our tasks accordingly.
'''
#importing other sub modules 
import dateandtime
import BorrowBooks
import ReturnBooks
import SplitList
Access=True         #set access as trur
while Access==True: #using while block for condition check
    print("      ----------------------------------------------------      ")
    print("      |            Elite Library Management              |      ")
    print("      ----------------------------------------------------      ")
    print("      ----------------------------------------------------      ")
    print("      | A writer only begins a book.A reader finishes it.|      ")
    print("      ----------------------------------------------------      ")
    print("")
    print("Option 1 --> To Display the available books.")
    print("Option 2 --> To Borrow the books.")
    print("Option 3 --> To Return the borrowed books.")
    print("Option 4 --> To Exit the system.")
    print()
    try:  #implementing try block
        option=int(input("Choose your desired option here: ")) #input the correct option
        print("")     #for breaking a line while printing
        if(option==1): #checking condition
            with open("books.txt","r") as file: #opening "books.txt"file in read mode
                line=file.read()      #extraction of data from each line
                print("---------------------------------------------")
                print("|Book Name,Author Name,Quantity,Cost/10 days|")
                print("---------------------------------------------")
                print()
                print(line)
                print()
                print("A book is the device to light the imagination. So take it.      ")
                print()
        elif(option==2):
            SplitList.splitlist() #calling splitlist()function from SplitList module
            BorrowBooks.borrowbooks()#calling borrowbooks()function from BorrowBooks module
        elif(option==3):
            SplitList.splitlist()#calling splitlist()function from SplitList module
            ReturnBooks.returnbooks()#calling returnbooks() function from ReturnBooks module
        elif(option==4):
            print("      ----------------------------------------------------      ")
            print("      |     Thank you for visiting us !! See you again.   |     ")
            print("      ----------------------------------------------------      ")
            Access=False  #setting access as false to terminate the loop
        else:
            print("We only have option from 1-4.") #error message for input of other integer except 1-4
    except ValueError:
        print("Please choose a valid option.")#error message for input of alphabets
        
        
    
