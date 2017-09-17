from add_friend import spy_add
from colorama import Fore, Back, Style, init
from globals import select_friend
def read_all() :
    select = select_friend()
    x = 0
    while x < len(spy_add[select].chats) :
        if spy_add[select].chats[x]['sent_by_me'] == True :
            print Fore.BLUE + spy_add[select].chats[x]['time'].strftime('%d, %b %y') + Fore.RED + " You :" \
            "" + Fore.BLACK + spy_add[select].chats[x]['message']
            x += 1
        else :
            print Fore.BLUE + spy_add[select].chats[x]['time'].strftime('%d, %b %y') + Fore.RED + " " + spy_add[select].name +\
            ":" + Fore.BLACK + spy_add[select].chats[x]['message']
            x += 1
    raw = raw_input("Press Enter to Continue ..............")