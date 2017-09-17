class Spy:
    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.name = self.salutation + ' ' + self.name
        self.spy_stat = None

spy = Spy('Harry Potter','Mr.',29,4.5)