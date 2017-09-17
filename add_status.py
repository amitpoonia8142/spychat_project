from spy_details import spy,Spy
import re
from globals import status
def spy_status() :
    print "\nSome old status are :- \n"
    i = 0
    length = len(status)
    while i < length :
            print    str(i + 1) + ". " + status[i]
            i += 1

    select = raw_input("you want to use existing status or create your own status (y/n) ")
    select_validation = '^[y,n]$'
    if (re.match(select_validation,select) != None):
        if select.upper() == "Y" :
            spy.spy_stat = raw_input("Enter your Status ")
            status.append(spy.spy_stat)
        else :
            i = int(raw_input('Select the no from the upper existing status '))
            spy.spy_stat = str(status[i-1])
    else :
        print "Invalid Details !!! Try Again"

    print "YOUR CURRENT STATUS = " + str(spy.spy_stat)
    raw = raw_input("\nPress any key to go back to main menu \n")