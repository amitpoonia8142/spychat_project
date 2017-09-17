from add_friend import friend_name, spy_add,Spy_friend
from globals import select_friend
from steganography.steganography import Steganography
from datetime import datetime
def send_message() :
    if len(friend_name)!= 0 :
        print "Select friend to send message"
        select = select_friend()
        original_image = raw_input("Enter the name of image in which we want to hide the message : ")
        output_image = raw_input("Name of the Output Image :  ")
        text = raw_input("The secret message : ")
        Steganography.encode(original_image, output_image, text)

        new_chat = {
            "message": text,
            "time": datetime.now(),
            "sent_by_me": True
        }
        spy_add[select].chats.append(new_chat)

    else :
        print "Add your friend first"
        raw = raw_input("Press any key to return to menu .......")