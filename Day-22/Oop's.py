'''

#Object-oriented Programming (OOP):

 => Object-Oriented Programming (OOP) in Python is a way of structuring code using classes and objects,
    making programs more modular, reusable, and easier to maintain.
 => The four main pillars are encapsulation, inheritance, polymorphism, and abstraction.

 1.Classes and Objects

  Class:- A blueprint for creating objects.

     class Dog:
        species = "Canine"   # Class attribute
        def __init__(self, name, age):
            self.name = name  # Instance attribute
            self.age = age


  Object:- An instance of a class.

     dog1 = Dog("Buddy", 3)
     print(dog1.name)     # Buddy
     print(dog1.species)  # Canine




 2.Encapsulation
 
 => Bundles data (attributes) and methods (functions) together.

 => Example: Protecting variables by using private attributes
     (_variable or __variable).


 3.Inheritance
 
 => Allows a class to reuse code from another class.

   class Animal:
    def speak(self):
        print("Some sound")

   class Dog(Animal):
    def speak(self):
        print("Woof!")


 4.Polymorphism
 
 => Same method name behaves differently depending on the object.

    for animal in [Dog(), Animal()]:
        animal.speak()
    # Output: Woof! / Some sound


 5.Abstraction

 => Hides implementation details, showing only essential features.

 => Achieved using abstract base classes (abc module).




class Flipkart:
    discound = 10
    products = ['laptop','phone','mouse','charger']

    @classmethod
    def showProducts(cls):
        print(cls.products)


    def login(self,username,password):
        self.username = username
        self.password = password
        print(f"welcome to the flipkart {self.username}")

    @staticmethod
    def banner():
        print("10% discount is going on flipkart, shop now!")

ramakanth = Flipkart()
ramakanth.login('ramakanth','ramakanth@1234')
ramakanth.banner()
ramakanth.showProducts()

Flipkart.showProducts()
Flipkart.banner()



#checking the username

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f"welcome to the Instagram, {self.username}")


vamsi = Instagram('vamsi','vasmi@1234')



#changing the username

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.followers = []
        print(f"welcome to the Instagram, {self.username}")


vamsi = Instagram('vamsi','vasmi@1234')

print("Before username:",vamsi.username)
vamsi.username = 'ramakanth'
print("After username:",vamsi.username)



#changing the password

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._followers = []

    def getpassword(self):
        return self.__password

    def setpassword(self,newpassword):
        self.__password = newpassword


vamsi = Instagram('vamsi','vasmi@1234')

print("Before username:",vamsi.username)
vamsi.username = 'ramakanth'
print("After username:",vamsi.username)

print("Before password:",vamsi.getpassword())
vamsi.setpassword('ramakanth@123')
print("After password:",vamsi.getpassword())


'''
