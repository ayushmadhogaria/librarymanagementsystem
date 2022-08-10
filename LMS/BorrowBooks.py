'''
This module helps us to borrow books and generate a borrow note in
Borrow file in Borrow folder.
'''
#importing other sub modules 
import SplitList
import dateandtime

def borrowbooks():  #defining function for the module
    access=False    #setting access as false
    while(True):    #using while loop for condition check
        f_name=str(input("Type in your First Name--> ")) #firstname input of borrower
        if f_name.isalpha():     #using isalpha() to check whether passed character is alphabet or not
            break
        print("Please enter valid input.")#error message incase of invalid input
    while(True):
        l_name=str(input("Type in your Last Name--> ")) #lastname input of borrower
        if l_name.isalpha():
            break
        print("Please enter valid input.")

    book="Books/"+"Book_"+f_name+".txt"   #creating file of name of books borrowed in Books folder
    borrow="Borrow/"+"BorrowBook_"+f_name+".txt" #creating borrow book details note in Borrow folder

    with open(borrow,"w+") as file:    #open the particular created borrow file in read and write mode
        file.write("      ----------------------------------------------------     "+"\n")
        file.write("      |            Elite Library Management              |     "+"\n")
        file.write("      ----------------------------------------------------     "+"\n\n")
        file.write("Name of the borrower -->" +" " + f_name + " " + l_name+"\n\n")
        file.write("Date of borrow -->" +" " +dateandtime.Date()+"\n")
        file.write("Time of borrow -->" +" " +dateandtime.Time()+"\n\n")
        file.write("S.N. \t\t\t Name of the book \t\t\t Name of the Author \t\t\t  Cost/10 days \n")
    total_cost=0.0    #set total cost as 0.0 in float data type
    while access==False: #using while loop for condition check
        print("Choose an option below for your desired books:")
        for k in range(len(SplitList.BookName)):
            print("Press",k,"to select the book ",SplitList.BookName[k]) #displaying the books options

        try:     #try block
            z=int(input()) #taking integer input for book selection
            if z<0:        #only taking positive integer
                print("Enter a positive number")
                print("")
                continue
            with open(book,"w") as fi: #open the book name file in write mode
                pass
            try:
                with open(book,"r") as fi: #open the book name file in read mode
                    fil=fi.read()       
                if(SplitList.BookName[z])in fil: #checking if the book name is present in book name file
                    print("Sorry! Same book cannot be borrowed twice.")#error message for borrwing same book
                    continue
                
                if(int(SplitList.Quantity[z])>0):   #checking the quantity of book
                    print("This book is available.")
                    total_cost+=float(SplitList.Cost[z]) #calculating total cost of books
                    with open(borrow,"a") as file:       #append the created borrow note file 
                        file.write("1) \t\t\t" + SplitList.BookName[z]+"\t\t\t\t"+SplitList.AuthorName[z]+"\t\t\t\tRs."+SplitList.Cost[z]+"\n")
                    with open(book,"a") as fi:
                        fi.write(SplitList.BookName[z]+"\n")
                    SplitList.Quantity[z]=int(SplitList.Quantity[z])-1 #decreasing the quantity of books in "books.txt" file
                    with open ("books.txt","w+") as file:     #open "books.txt" file in read and write mode
                        for k in range(7):
                            file.write(SplitList.BookName[k]+","+SplitList.AuthorName[k]+","+str(SplitList.Quantity[k])+","+"Rs."+SplitList.Cost[k]+"\n")

                    #for borrowing more books
                    iterate=True   #starting loop iterate
                    number=1       #initializing number=1
                    while iterate==True:  #while loop for condition check
                        option=str(input("Wishing to borrow more books? Type in Yes or No here."))
                        if(option.upper()=="YES"):
                            number=number+1 #auto increasing the S.N in the text file
                            print("          Remember that same book cannot be borrowed again.")
                            print()
                            print("Choose an option below for desired books: ")
                            for k in range(len(SplitList.BookName)):
                                print("Press",k,"to select the book you need",SplitList.BookName[k])
                            z=int(input())
                            with open(book,"r") as fi:
                                fil=fi.read()
                            if(SplitList.BookName[z])in fil:
                                number=number-1#decreasing the S.N number if same book is borrowed
                                print("Sorry! Same book cannot be borrowed twice. ")
                                continue
                            if(int(SplitList.Quantity[z])>0):
                                print("This book is available in stock.")
                                total_cost+=float(SplitList.Cost[z]) # calculating total cost of multiple books
                                with open(borrow,"a") as file:       #append the created file with more imformation
                                    file.write(str(number)+") \t\t\t"+SplitList.BookName[z]+"\t\t\t\t"+SplitList.AuthorName[z]+"\t\t\t\t Rs."+SplitList.Cost[z]+"\n")
                                    SplitList.Quantity[z]=int(SplitList.Quantity[z])-1
                                with open(book,"a") as fi:
                                    fi.write(SplitList.BookName[z]+"\n")
                                with open("books.txt","w+") as file:
                                    for k in range(7):
                                        file.write(SplitList.BookName[k]+","+SplitList.AuthorName[k]+","+str(SplitList.Quantity[k])+","+"Rs."+SplitList.Cost[k]+"\n")
                                        access=False #terminate the loop

                            else:
                                iterate=False  #terminate the loop 
                                break
                        elif (option.upper()=="NO"):
                            print("")
                            iterate=False
                            access=True
                        else:
                            print("You can only reply with Yes or No.") #if the input is other than yes or no 
                else:
                    print("Sorry!! This book is out of stock.")  #output when Quantity of book is less than 1
                    borrowbooks()
                    access=False

            except IndexError: #if the input is other positive integer except the given books number
                print("")
                print("Only the above mentioned book numbers are acceptable.")
        except ValueError: # if input is not integer 
            print("")
            print("Invalid choice.")
    with open(borrow,"a") as file:  # append file with Total which shows total price
        file.write("\n \t\t\t\t\t\t\t\t\t\t\t\t\t Total:"+"Rs."+str(total_cost))
    with open(borrow,"r") as file:  #display created note file in shell
        print(file.read())

    print("                         -----------------------------------------                ")
    print("                               Thank you!! Enjoy Reading.                         ")
    print("                         -----------------------------------------                ")
                                
                   
                    
    

    
    
        
