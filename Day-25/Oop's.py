'''

#Banks Account

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def checkbalance(self):
        print("You can checkout your balance")

    def viewhistory(self):
        print("You can your transactions")

    def userinfo(self):
        print("You can see your details")

    def transactions(self):
        print("You can transfer money through netbanking")

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class CurrentAccount(BankAccount):
    def deposit(self):
        print("You can deposit - CA")
    def withdraw(self):
        print("You can withdraw - CA")

class SavingAccount(BankAccount):
    def deposit(self):
        print("You can deposit - SA")
    def withdraw(self):
        print("You can withdraw - SA")

class FixedDeposit(BankAccount):
    def deposit(self):
        print("You can deposit - FD")
    def withdraw(self):
        print("You can withdraw - FD")
        
class SalaryAccount(BankAccount):
    def deposit(self):
        print("You can deposit - SAA")
    def withdraw(self):
        print("You can withdraw - SAA")

class ZeroBalanceAccount(BankAccount):
    def deposit(self):
        print("You can deposit - ZBA")
    def withdraw(self):
        print("You can withdraw - ZBA")


amathya = ZeroBalanceAccount()
amathya.deposit()
amathya.withdraw()
amathya.checkbalance()
amathya.viewhistory()
amathya.userinfo()
amathya.transactions()


ramakanth = SalaryAccount()
ramakanth.deposit()
ramakanth.withdraw()
ramakanth.checkbalance()
ramakanth.viewhistory()
ramakanth.userinfo()
ramakanth.transactions()



#Using the OOP's to write the train management

from abc import ABC, abstractmethod

#Encapsulation
class Passenger:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


#Abstraction
class Train(ABC):
    @abstractmethod
    def book_ticket(self):
        pass


#Inheritance
class ExpressTrain(Train):
    def __init__(self, train_name, fare):
        self.train_name = train_name
        self.fare = fare

#Polymorphism
    def book_ticket(self):
        print(f"Ticket booked in {self.train_name}")
        print(f"Fare: ₹{self.fare}")


class SuperFastTrain(Train):
    def __init__(self, train_name, fare):
        self.train_name = train_name
        self.fare = fare

#Polymorphism
    def book_ticket(self):
        print(f"Ticket booked in {self.train_name}")
        print(f"Fare: ₹{self.fare}")


#Main Program
p = Passenger("Amathya Reddy", 22)

print("Passenger Details")
print("Name:", p.get_name())
print("Age :", p.get_age())

print("\nChoose Train")
print("1. Express Train")
print("2. SuperFast Train")

choice = int(input("Enter choice: "))

if choice == 1:
    train = ExpressTrain("Express 101", 500)
elif choice == 2:
    train = SuperFastTrain("SuperFast 202", 900)
else:
    print("Invalid Choice")
    exit()

print("\nBooking Details")
train.book_ticket()



#Bus Booking Management

from abc import ABC, abstractmethod

class BusBooking(ABC):
    def checkavailability(self):
        print("You can check Bus seat availability")

    def passengerdetails(self):
        print("You can view passenger details")

    def ticketstatus(self):
        print("You can check ticket status")

    def cancelticket(self):
        print("You can cancel your ticket")

    @abstractmethod
    def bookticket(self):
        pass
    @abstractmethod
    def fare(self):
        pass


class ExpressBus(BusBooking):

    def bookticket(self):
        print("Ticket booked in Express Bus")
    def fare(self):
        print("Fare: ₹500")


class SuperFastBus(BusBooking):

    def bookticket(self):
        print("Ticket booked in SuperFast Bus")
    def fare(self):
        print("Fare: ₹800")


class ShivaTravelsBus(BusBooking):

    def bookticket(self):
        print("Ticket booked in Shiva Travel Bus")

    def fare(self):
        print("Fare: ₹1500")



prakash = ShivaTravelsBus()
prakash.bookticket()
prakash.fare()
prakash.checkavailability()
prakash.passengerdetails()
prakash.ticketstatus()
prakash.cancelticket()

print("-----------------------")

naresh = SuperFastBus()
naresh.bookticket()
naresh.fare()
naresh.checkavailability()
naresh.passengerdetails()
naresh.ticketstatus()
naresh.cancelticket()

'''

class Redbus:
    busno = 'cg001'
    driver_name = 'xyz'
    driver_phonenumber = 9381592725
    seats = {}
    for i in range(1,11):
        if i%2==0:
            seats[i] = 'Available'
        else:
            seats[i] = 'Booked'

    def __init__(self,name,phonenumber,age):
        self._name = name
        self._phonenumber = phonenumber
        self._age = age
        print(f"Welcome to the Redbus {self._name}. Book your bus")
        
            
    @classmethod
    def showseats(cls):
        for i in cls.seats:
            print(i,cls.seats[i])

    def booking(self,seatno):
        if Redbus.seats[seatno] == 'Available':
            Redbus.seats[seatno] = 'Booked'
            print(f"{seatno} is successfully booked")
            Redbus.driverinfo()
        else:
            print(f"{seatno} is already booked")

    @staticmethod
    def driverinfo():
        print("Driver's info")
        print("Bus no :",Redbus.busno)
        print("driver Name:",Redbus.driver_name)
        print("driver Phonenumber:",Redbus.driver_phonenumber)


achyuth = Redbus('achyuth',9603031890,22)
achyuth.showseats()
achyuth.booking(2)
achyuth.showseats()
    
