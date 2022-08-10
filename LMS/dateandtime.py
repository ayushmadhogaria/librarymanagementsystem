'''
Datetime module
This module is for getting the exact actual time and date when the
books is borrowed or returned by the particular person.
It will be imported and used in modules where books will be
borrowed and returned.
'''
import datetime               #importing datetime from library
#method for getting date
def Date():          
    now=datetime.datetime.now #for getting current date and time
    return str(now().date())  #returning the date value from now

#method for getting time
def Time():
    now=datetime.datetime.now  #for getting the current date and time
    return str(now().time())   #returning the time value from now
