'''

#Not a PreminumHotstar

class Hotstar:
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the hotstar")
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You can select the languages")
    def playcontrollers(self):
        print("You can pause and play the video")
    def ads(self):
        print("Ads will run")
    def movies(self):
        print("You can limited access for movies")
    def sports(self):
        print("Limited time you can watch sports")
    def quality(self):
        print("limited quality")


achyuth = Hotstar('achyuth')
achyuth.login()
achyuth.dashboard()
achyuth.search()
achyuth.languages()
achyuth.playcontrollers()
achyuth.ads()
achyuth.movies()
achyuth.sports()
achyuth.quality()




#Premium Hotstar
        
class PremiumHotstar():
    def __init__(self,name):
        self.name = name
        print(f"Hi {self.name}, Welcome to the premiumhotstar")
    def login(self):
        print("You can login")
    def dashboard(self):
        print("You can see the dashboard items")
    def search(self):
        print("You can search")
    def languages(self):
        print("You can select the languages")
    def playcontrollers(self):
        print("You can pause and play the video")
    def ads(self):
        print("Ads won't run")
    def movies(self):
        print("You can unlimited access for movies")
    def sports(self):
        print("You can watch sports")
    def quality(self):
        print("High quality")
        

amathya = PremiumHotstar('amathya')
amathya.login()
amathya.dashboard()
amathya.search()
amathya.languages()
amathya.playcontrollers()
amathya.ads()
amathya.movies()
amathya.sports()
amathya.quality()

'''


#Overloading

class Number:
    def __init__(self,n):
        self.n = n
    def __add__(self,other):
        return self.n + other.n
    def __sub__(self,other):
        return self.n - other.n
    def __mul__(self,other):
        return self.n * other.n
    def __truediv__(self,other):
        return self.n / other.n
    def __eq__(self,other):
        return self.n == other.n
    def __lt__(self,other):
        return self.n < other.n
    def __gt__(self,other):
        return self.n > other.n
    def __str__(self):
        return str(self.n)
    

n1 = Number(10)
n2 = Number(20)
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1==n2)
print(n1<n2)
print(n1>n2)
print(n1,n2)
