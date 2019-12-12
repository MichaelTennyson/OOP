# lab test 2
# c18302166 - michael tennyson
# date: 12/12/19
# the following code consists of methods that create a 3D vector
# the class vector consists of arithmetic
# operators that adds, subtracts, multiplies and finds the magnitude of the vector


# class initialisation
class Vector3D():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)
# methods consisting of arithmetic operations

    def add(self, x, y, z):
        return __class__(self.x + self.x, self.y + self.y, self.z + self.z)

    def subtract(self, x, y, z):
        return __class__(self.x - self.x, self.y - self.y, self.z - self.z)

    def multiply(self, x, y, z):
        return __class__(self.x * self.x, self.y * self.y, self.z * self.z)

    def magnitude(self, x, y, z):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (.5)

    def print(self):
        print(self.x, self.y, self.z)

# method calls

vector1 = Vector3D(9, 7, 6)

v1_add = vector1.add
v1_sub = vector1.subtract
v1_multiply = vector1.multiply
v1_mag = vector1.magnitude

print(v1_add)
print(v1_sub)
print(v1_multiply)
print(v1_mag)



