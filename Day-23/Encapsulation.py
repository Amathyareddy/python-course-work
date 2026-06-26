'''

class Instagram:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.followers = []

    def getpassword(self):
        return self.__password

    def setpassword(self, newpassword):
        self.__password = newpassword


praveen = Instagram("praveen", "Praveen@123")

# Username
print("Before username:", praveen.username)
praveen.username = "praveenkumar"
print("After username:", praveen.username)

# Password
print("Before password:", praveen.getpassword())
praveen.setpassword("praveenkumar@123")
print("After password:", praveen.getpassword())



class Instagram:
    def __init__(self):
        self._post = []

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        self._post.append(newpost)

praveen=Instagram()
print(praveen.accesspost)
praveen.accesspost = 'class and object'
print(praveen.accesspost)

'''









