'''
This module helps to return the borrowed book with generation of
return note in Return folder.
'''
#import other sub modules 
import SplitList
import dateandtime
def returnbooks(): #defining function for the module
    firstname=str(input("Type in your First Name --> ")) # input the first name
    borrowb="Borrow/"+"BorrowBook_"+firstname+".txt" 
    try:
        with open(borrowb,"r") as file:#open the borrow file of this name in read mode
            l=file.readlines()         #read all the lines of file in single go
            l=[borrowb.strip("Rs.") for borrowb in l] #remove the "Rs." from file 
        with open(borrowb,"r") as file:
            a=file.read()     #read the file
            print(a)        #print the file in shell
    except:
        print("Borrower of this name doesn't exist.") #incase of invalid input
        returnbooks()

    returnbook="Return/"+"ReturnBook_"+firstname+".txt" #create return note file in Return folder
    with open(returnbook,"w+") as file:   #open the created return note file in read and write mode
        file.write("      ----------------------------------------------------     "+"\n")
        file.write("      |            Elite Library Management              |     "+"\n")
        file.write("      ----------------------------------------------------     "+"\n\n")
        file.write("Name of person returning the book -->" +" " + firstname+"\n\n")
        file.write("Date of return -->" +" " +dateandtime.Date()+"\n")
        file.write("Time of return -->" +" " +dateandtime.Time()+"\n\n")
        file.write("S.N. \t\t\t Name of the book \t\t\t Name of the Author \t\t\t  Cost/10 days \n")

    total_cost=0.0  #initializing total as 0.0 in float data type
    n=0
    for k in range(7):
        if SplitList.BookName[k] in a:
            n=n+1
            with open(returnbook,"a") as file:  #opening return note file in append mode
                file.write(str(n)+")\t\t\t"+SplitList.BookName[k]+"\t\t\t"+SplitList.AuthorName[k]+"\t\t\t\t Rs."+SplitList.Cost[k]+"\n\n")
                SplitList.Quantity[k]=int(SplitList.Quantity[k])+1
            total_cost+=float(SplitList.Cost[k])  #calculating total cost of book

    print("Are you delayed in returning the book? Type in yes or no.")

    while(True): #if book return is delayed
        option=str(input()) #string input
        if(option.upper()=="YES"): 
            print("Fine will be imposed accordingly. Type in the number of days by which the return is delayed.")
            delay=int(input()) #input of days of delay return
            #condition used to impose fine 
            if(delay<=7):       #for book returned within 7 days of delay
                fine_amount=(5/100)*total_cost
            elif(delay>7 and delay<=15):  #return in between 7 to 15 days
                fine_amount=(10/100)*total_cost
            elif(delay>15 and delay<=25):  #return in between 15 to 25 days
                fine_amount=(20/100)*total_cost
            elif(delay>25 and delay<=30):    #return in betweeb 25 to 30 days
                fine_amount=(50/100)*total_cost 
            else:
                fine_amount=(80/100)*total_cost  # return for more than 30 days
            with open(returnbook,"a") as file:   #append returnbook file to write fine amount
                file.write("\t\t\t\t\t\t\t\t\t\t\t\t Fine amount: Rs."+str(fine_amount)+"\n")
            total_cost=total_cost+fine_amount  #adding fine in total cost
            print()
            print("Amount of fine imposed --> Rs." +str(fine_amount))
            print("Total amount to be paid --> Rs." +str(total_cost))
            break
        elif(option.upper()=="NO"):  #incase book return is not delayed
            fine_amount=0            #fine is 0
            print("No fine will be imposed.")
            print("Amount of fine imposed --> Rs." +str(fine_amount))
            print("Total amount to be paid --> Rs." +str(total_cost))
            with open(returnbook,"a") as file:   #append returnbook file to write fine as 0
                file.write("\t\t\t\t\t\t\t\t\t\t\t\t Fine amount: Rs."+str(fine_amount)+"\n")
            break
        else:
            print("You can only reply with Yes or No.") #incase of invalid input

    with open(returnbook,"a") as file:  #append returnbook file for adding Total Cost with fine
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t Total cost: Rs."+str(total_cost))

    with open("books.txt","w+") as file:
        for k in range(7):
            file.write(SplitList.BookName[k]+","+SplitList.AuthorName[k]+","+str(SplitList.Quantity[k])+","+"Rs."+SplitList.Cost[k]+"\n")

    with open(returnbook,"r") as file:  #printing the return book note in shell
        print(file.read())

    print("                         -----------------------------------------                ")
    print("                               Thank you!! Enjoy Reading.                         ")
    print("                         -----------------------------------------                ")
                       
            
                
                
        
    
