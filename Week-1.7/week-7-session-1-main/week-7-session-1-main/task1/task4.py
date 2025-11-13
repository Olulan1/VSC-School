# Define a class Book with the following fields:
# (1) title - the book title
# (2) author - the author(s) of the book
# (3) ISBN - the International Standard Book Number, which is 10-13 digits long
# (4) availability - whether the book is available (True or False)
# When an instance of a Book is created, only the value to the first three fields are required
# for the __init__ method as the book is available when created.

class Book():

    def __init__(self, title= "", author = "", ISBN="0000000000000", availability = True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability

    def setAvailability(self, input):
        self.avaiability = input


# Once completed, create two instances of Book with the details of two of your favourite books.
# Write code to print the details of each books
book1 = Book("The Elementia Chronicles", "Sean Fay Wolfe", "9780008152864")

book2 = Book("Kagerou Daze: Vol. 1", "Jin", "9780316259491", False)