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
class BankAccount:
    def set_details(self, name, balance = 0 ):
        self.name = name
        self.balance = balance

    def display(self):
        print('Name:', self.name)
        print('Balance:', self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

account1 = BankAccount()
account1.set_details('Nabeel', 1000)

account1.display()

account1.withdraw(200)
account1.deposit(500)
account1.display()