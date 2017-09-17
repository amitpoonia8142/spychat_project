
import re
class Spy_friend:
    def __init__(self):
        self.name = ''
        self.salutation = ''
        self.age  = ''
        self.rating = ''
        self.is_online = True
        self.chats = []
        self.name = self.salutation + ' ' + self.name
        self.spy_stat = None
spy_add = []
friend_name = []

def add_friend() :
    i = []
    count = 0
    stat = True
    while stat :
        i.append(Spy_friend())
        x = 0
        print "your friends"
        while x < len(friend_name) :
            print str(x+1) + ". " + spy_add[x].name
            x += 1
        i[count].name = raw_input('What is your friend\'s name ? ')
        if len(i[count].name) > 0:
            # name length cannot be null
            name_validation = '^[a-zA-z]+\s*[a-zA-z\s]*$'
            # name should be in alphabets only

            if (re.match(name_validation, i[count].name) != None):

                i[count].salutation = raw_input('What do we like to call him Mr./Ms./Agent/Dr. ')
                i[count].age = raw_input('What is his/her age ? ')
                age_validation = '^[0-9]{1,3}$'
                if (re.match(age_validation, i[count].age) != None):
                    # checking whether the age is in integer type or not
                    i[count].age = int(i[count].age)
                    # converting spy_age fro string to age
                    if (i[count].age > 12 and i[count].age < 50):
                        # the spy age should be in between 12 to 50 years
                        i[count].rating = raw_input('What is his rating ')

                        rating_validation = '^[0-9]{1,2}[.][0-9]{1,2}$'
                        if (re.match(rating_validation, i[count].rating) != None):
                            # checking whether the rating is in the form of float
                            i[count].rating = float(i[count].rating)
                            if (i[count].rating > 0.0 and i[count].rating < 10.0):
                                # spy rating must be in between 0.0 to 10.0
                                friend_name.append(i[count].name)
                                i[count].name = i[count].salutation + " " + i[count].name
                                spy_add.append(i[count])
                                count += 1
                                option = raw_input( 'add more friends (y/n)' )
                                if option.upper() == 'Y':
                                    stat = True
                                else :
                                    stat = False
                            else:
                                print 'Spy rating must be in between 0.0 to 10.0'
                        else:
                            print 'Invalid details !!!!!! Spy Rating must be provided in the form of float'
                    else:
                        print 'he/she not eligible for a spy according to his/her age'
                else:
                    print 'Spy age must be in integers '
            else:
                print 'Invalid details. Name provided is in incorrect pattern'
        else:
            print 'name cannot be empty'