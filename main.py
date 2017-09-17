#importing all the variables we want
from start_chat import start_application
from spy_details import  spy,Spy
import re
from colorama import Fore, Back, Style, init
init(autoreset=True)

#let's start the application
print 'Let\'s get Started...'
#taking input
answer = raw_input("Do you want to continue as " + spy.salutation + " " + spy.name + "(y/n) ")
if answer.upper()=='N' :
    spy_name = raw_input('What is your name ? ')
    if len(spy_name) > 0 :
    #name length cannot be null
        name_validation = '^[a-zA-z]+\s*[a-zA-z\s]*$'
        #name must be of alphabets only

        if (re.match(name_validation, spy_name) != None) :
            spy_salutation = raw_input('What do we call you Mr./Ms. ')
            spy_age =  raw_input('What is your age ? ')
            age_validation = '^[0-9]{1,3}$'
            if (re.match(age_validation, spy_age) != None) :
                #checking the age is in integer type or not
                spy_age = int(spy_age)
                #converting spy_age fro string to age
                if (spy_age > 12 and spy_age < 50) :
                    #the spy age must be in between 12 to 50 years
                    spy_rating = raw_input('What is your rating ')
                    rating_validation = '^[0-9]{1,2}[.][0-9]{1,2}$'
                    if (re.match(rating_validation, spy_rating) != None) :
                        #checking whether the rating is in the form of float
                        spy_rating = float (spy_rating)
                        if (spy_rating > 0.0 and spy_rating < 5.0) :
                            #spy rating must be in between 0.0 to 5.0
                            spy = Spy(spy_name, spy_salutation, spy_age, spy_rating)
                            print Fore.MAGENTA + 'Welcome ' + spy.name + ' we are glad you are back'
                            start_application()

                        else :
                            print 'Spy rating must be in between 0.0 to 5.0'
                    else :
                        print 'Invalid details !!!!!! Spy Rating must be provided in the form of float'
                else :
                    print 'You are not eligible for a spy according to your age'
            else :
                print 'Spy age must be in integers '
        else :
            print 'Invalid details. Name provided is in incorrect pattern'
    else :
        print 'Name cannot be empty.'

elif answer.upper()=='Y':
    print Fore.MAGENTA + 'Welcome '  + spy.name + ' we are glad you are back'
    start_application()
