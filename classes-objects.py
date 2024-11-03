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
class Product:
    def __init__(self):
        self.data1 = 10
        self.__data2 = 100
    def method1(self):
        print('Method 1')
    def __method2(self):
        print('Method 2')

p = Product()
print(p._Product__method2())