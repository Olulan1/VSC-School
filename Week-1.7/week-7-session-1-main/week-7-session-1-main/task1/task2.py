# Identify and correct the errors in the following class definition.

class Rectangle:
    def __init__(self, width, height):
       self.height  = height
       self.width= width

    def set_height(self, height):
        self.height = height

    def set_width(self, wid):
        self.width= wid


# Once corrected, we can now create an instance of Rectangle
# and print the details of the class
rectangle1 = Rectangle(5, 8)
print(rectangle1.height)
print(rectangle1.width)

# we can also call the method
rectangle1.set_height(10)
print(rectangle1.height)
