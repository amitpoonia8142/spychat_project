from spy_details import Spy , spy
from read_all import read_all

from add_status import spy_status
from add_friend import add_friend
from send_msg import send_message
from read_message import read_message
import re
from colorama import Fore, Back, Style, init
init(autoreset=True)
def start_application () :
    print   ' Your details : - ' \
            '\n Name : ' + spy.name +\
            '\n Age : ' + str(spy.age) +\
            '\n Rating : ' + str(spy.rating) +\
            '\n Is online : ' + str(spy.is_online)
    raw = raw_input("Press enter to continue .........")
    status = True
    while status :
        print   '\n\nMenu  Select one of the following '\
                '\n1.Add a status update' \
                '\n2.Add a friend' \
                '\n3.Send a Secret message' \
                '\n4.Read a secret message' \
                '\n5.Read chats from user' \
                '\n6.Close Application'
        choice = raw_input('Enter your choice :- ')
        choice_validation = '^[1-6]$'
        if (re.match(choice_validation, choice) != None) :
            choice = int(choice)
            if choice == 1 :
                #add a status section
                spy_status()
            elif choice == 2 :
                #add a friend
                add_friend()
            elif choice == 3 :
                #Send a secret message
                send_message()
            elif choice == 4 :
                #Read a secret message
                read_message()
            elif choice == 5 :
                #Read chat form use
                read_all()
            elif choice == 6 :
                #close the application

                status = False
        else :
            print Fore.RED + 'You have entered a wrong choice \n'
            raw = raw_input("Press any key to continue ..........")