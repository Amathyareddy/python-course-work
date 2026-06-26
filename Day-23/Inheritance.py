'''

#Inheritance in Python:

Inheritance is an OOP concept where one class (child class) acquires the properties (attributes) and behaviors (methods) of another class (parent class)
It promotes code reusability, because the child class can use the code already written in the parent class.


#Types of inheritence
1.single inheritance:
    One parent → One child
    
2.multiple inheritance:
    One child inherits from more than one parent.
    Father    Mother
    \      /
      Child
    
3.multilevel inheritance:
    Inheritance in multiple levels.
4. Hierarchical Inheritance:
    One parent → Multiple children.
5. Hybrid Inheritance:
    A combination of two or more types of inheritance.



#whatsapp

#1.single inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def call(self):
        print("You can do video/audio calls")

praveen=whatsappv1()
print("v1-praveen")
praveen.message()


naresh=whatsappv2()
print("v2-naresh")
naresh.message()
naresh.call()



#multiple inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2:
    def call(self):
        print("You can do video/audio calls")

class whatsappv3:
    def media(self):
        print("You can share your photos/videos")

class whatsappv4(whatsappv1, whatsappv2, whatsappv3):
    def status(self):
        print("You can share status-[24 hours]")

praveen = whatsappv4()
print('v4- praveen')

praveen.message()
praveen.call()
praveen.media()
praveen.status()



#Multilevel inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages")

class whatsappv2(whatsappv1):
    def call(self):
        print("You can make audio/video calls")

class whatsappv3(whatsappv2):
    def media(self):
        print("You can share photos and videos")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can share status (24 hours)")


praveen = whatsappv4()
print('v2- praveen')

praveen.message()
praveen.call()
praveen.media()
praveen.status()



class whatsappv1:
    def message(self):
        print("You can send messages")

class whatsappv2(whatsappv1):
    def call(self):
        print("You can make audio/video calls")

class whatsappv3(whatsappv2):
    def media(self):
        print("You can share photos and videos")

class whatsappv4(whatsappv3):
    def status(self):
        print("You can share status (24 hours)")


praveen = whatsappv1()
print('v1- praveen')
praveen.message()

praveen = whatsappv2()
print('v2- praveen')
praveen.message()
praveen.call()

praveen = whatsappv3()
print('v3- praveen')
praveen.message()
praveen.call()
praveen.media()

praveen = whatsappv4()
print('v4- praveen')

praveen.message()
praveen.call()
praveen.media()
praveen.status()



# Hierarchical Inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")

pandu = whatsappv3()
print("v3")
pandu.message()
pandu.stickers()

pandu = whatsappv2()
print("v2")
pandu.message()
pandu.emojis()

pandu = whatsappv1()
print("v1")
pandu.message()



#Hibrid inheritance:

class whatsappv1:
    def message(self):
        print("You can send messages to people")

class whatsappv2(whatsappv1):
    def emojis(self):
        print("You can send messages with emojis to people")

class whatsappv3(whatsappv1):
    def stickers(self):
        print("You can send messages with stickers to people")

class whatsappv4(whatsappv3,whatsappv2):
    def gif(self):
        print("You can send messages with gif to people")

pandu = whatsappv4()
print("v4")
pandu.message()
pandu.stickers()
pandu.emojis()
pandu.gif()



#Method Overriding:

#Method Overriding using super

class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2(wpv1):
    def status(self):
        super().status()
        print("You can react and reply")

class wpv3(wpv2):
    def status(self):
        super().status()
        print("You can like and reshare")

chanu = wpv3()
chanu.status()



#with out super class:

class wpv1:
    def status(self):
        print("You can upload images/videos")

class wpv2:
    def status(self):
        print("You can react and reply")

class wpv3(wpv2,wpv1):
    def status(self):
        wpv1.status(self)
        wpv2.status(self)
        print("You can like and reshare")

praveen= wpv3()
praveen.status()

'''



