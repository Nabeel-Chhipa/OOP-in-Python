# Exercise 1

# class Car:
#     def basicFeatures(self, color, wheels, seats, company):
#         self.color = color
#         self.wheels = wheels
#         self.seats = seats
#         self.company = company
#         print('Color: ', self.color, '\nWheels: ', self.wheels, '\nSeats: ', self.seats, '\nCompany: ', self.company)

# car1 = Car()
# car1.basicFeatures('Black', 4, 5, 'Hoda')

# car2 = Car()
# car2.basicFeatures('Sliver', 4, 2, 'BMW')


# Exercise 2
# class BankAccount():
#     def __init__(self, name, balance = 0):
#         self.name = name
#         self.balance = balance
#     def display(self):
#         print('Name: ', self.name, '\nBalance', self.balance)
#     def withdraw(self, amount):
#         self.balance -= amount
#     def deposit(self, amount):
#         self.balance += amount

# account1 = BankAccount('Nabeel', 1000)
# # account1.set_details('Nabeel', 1000)
# account1.display()
# account1.withdraw(300)
# account1.display()
# account1.deposit(600)
# account1.display()

# Exercise 3
# class Products:
#     def __init__(self):
#         self.data1 = 10
#         self.__data2 = 20
#     def method1(self):
#         pass
#     def __method2(self):
#         print('Method 2')
# p1 = Products()
# print(p1._Products__method2())


# Property Decorators
class Emplooyee:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
        # self.email = first + last + '@gmail.com'

    @property
    def email(self):
        return f'{self.firstName}{self.lastName}@gmail.com'
    
    @property
    def fullName(self):
        return f'{self.firstName} {self.lastName}'
    
    @fullName.setter
    def fullName(self, name):
        first, last = name.split()
        self.firstName = first
        self.lastName = last

e1 = Emplooyee('Nabeel', 'Saleem')
print(e1.fullName)
e1.fullName = 'Usama Ramzan'
print(e1.fullName)