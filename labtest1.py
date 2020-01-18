# lab test1: pascal triangle
# author: michael tennyson
# date 24/10/19

# function that makes the pascal triangle and displays it
def make_new_row(choice):
   old_row = [1]
   y = [0]
   line_list = [old_row]

    # the following for loop adds the first number in the first line together
    # this is done iteratively to form the pascal triangle
    # the pascal triangle is assigned each row in the pascal triangle as a string, creating the triangle
    # the purpose of the zip function in the code is to pass the numbers being added to each row and return a new row that is a tuple
   for i in range(choice - 1):
      pascal_triangle = ' '.join([str(i) for i in old_row])
      print(pascal_triangle.center(100))
      old_row = [l + r for l, r in zip(old_row + y, y + old_row)]
      line_list = line_list + [old_row]

   print(line_list)

number = int(input("enter the number for the desired height of your pascal triangle\n"))

# error checking if statements, preventing a user from entering any other character except numbers
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYYX'
if number == "":
    print("you did not enter a number\n")
# error checking to see if the user has entered a letter
elif number in list(alpha):
    print("you cannot enter a letter\n")
else: # function call
    make_new_row(number)
