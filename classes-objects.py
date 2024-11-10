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
# class Emplooyee:
#     def __init__(self, first, last):
#         self.firstName = first
#         self.lastName = last
#         # self.email = first + last + '@gmail.com'

#     @property
#     def email(self):
#         return f'{self.firstName}{self.lastName}@gmail.com'
    
#     @property
#     def fullName(self):
#         return f'{self.firstName} {self.lastName}'
    
#     @fullName.setter
#     def fullName(self, name):
#         first, last = name.split()
#         self.firstName = first
#         self.lastName = last

# e1 = Emplooyee('Nabeel', 'Saleem')
# print(e1.fullName)
# e1.fullName = 'Usama Ramzan'
# print(e1.fullName)


# TASK 1
# class Book:
    # def __init__(self, isbn, title, author, publisher, pages, price, copies):
    #     self.isbn = isbn
    #     self.title = title
    #     self.author = author
    #     self.publisher = publisher
    #     self.pages = pages
    #     self.price = price
    #     self.copies = copies

    # def display(self):
        # data = [self.isbn, self.title, self.price, self.copies]
        # return data

    # def in_stock(self):
    #     if(self.copies > 0):
    #         print('True')
    #     else:
    #         print("False")

    # def sell(self):
    #     if(self.copies > 0):
    #         self.copies -= 1
    #     else:
    #         print("The book is out of stock.")

# book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 200,10)
# book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
# book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
# book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

# print(book1.display())
# print(book1.in_stock())
# print(book1.sell())


# TASK 2 ---------------------------
class Book:
    books = [
        {
            "title": "Learn Physics",
            "author": "Stephen" 
        },
        {
            "title": "Learn Chemistry",
            "author": "Jack" 
        },
        {
            "title": "Learn Maths",
            "author": "John" 
        },
        {
            "title": "Learn Biology",
            "author": "Jack" 
        },
    ]

    def display(self):
        for book in self.books:
            print(book)

book = Book()
book.display()