from add_friend import spy_add
from steganography.steganography import Steganography
from datetime import datetime
from globals import select_friend

def read_message():

    select = select_friend()
    image = raw_input("Name of the image in which message is hidden")
    msg = Steganography.decode(image)


    new_chat = {
        "message": msg,
        "time": datetime.now(),
        "sent_by_me": False
    }
    spy_add[select].chats.append(new_chat)