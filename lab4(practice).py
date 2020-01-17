# the following program writes a text file to a file object
# the program then takes a users input
# the input is written to the text file
# the string in the text file is then scrambled
# the text is displayed


file_obj = ('file.txt', 'w')
import random

print("this program will scramble the words of a text file\n")

string_list = list(file_obj)

for i in range(len(string_list)):
    random.shuffle(string_list)

file_obj = ''.join(string_list)
print("the scrambled word : ", file=file_obj)

file_obj.close()


