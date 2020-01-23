class Rectangle(object):
    def __init__(self, length,width):
        self.length = length
        self.width = width

    def perimeter(self):
       self.rectangle_perimeter = (self.length * 2) + (self.width * 2)

    def area(self):
         self.rectangle_area = self.length * self.width

    def __str__(self):
        return 'the area is {} and the perimeter is {}'.format(self.rectangle_area, self.rectangle_perimeter)


r1 = Rectangle(5, 8)
print(r1.area())
print(r1.perimeter())
