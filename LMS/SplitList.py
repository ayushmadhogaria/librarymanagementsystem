'''
This module helps us to remove the spaces and specified characters
in the "books.txt" text file using strip()function. Similarly, we
have used split()function to divide the text file into lists using
separation characters.
'''

#defining the method for SplitList module
def splitlist():
    #declaring the variables as global to access it from all modules 
    global BookName
    global AuthorName
    global Quantity
    global Cost
    #creating empty lists
    BookName=[]
    AuthorName=[]
    Quantity=[]
    Cost=[]
    with open("books.txt","r") as file:#opening the "books.txt" file in read mode

        l=file.readlines()             #reading lines of the file
        l=[u.strip('\n') for u in l]   #removing spaces of the textfile using strip()method
        for k in range(len(l)):        #using for loop
            value=0
            for z in l[k].split(','):   #using split() function to divide strings into lists
                if(value==0):
                    BookName.append(z)  #append the BookName list if value==0
                elif(value==1):
                    AuthorName.append(z) #append the AuthorName list if value==1
                elif(value==2):
                    Quantity.append(z)  #append the Quantity list if value==2
                elif(value==3):
                    Cost.append(z.strip("Rs.")) #append the Cost list if value==3 and using strip() function to remove Rs. from list
                value+=1                        
            
