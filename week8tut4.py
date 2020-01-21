# the following program prompts a user to enter a country and its capital
# takes a users input and puts it in a dictionary
# and iterates this again

# function checks if the user has entered yes or no, repeating the program
def check_input(input):
    if input == 'y' or input == 'n':
        return  True
    return False

capitals = {}

country_str = input('enter a country\n')
country_cap = input('enter the capital of the country you just entered\n')
capitals[country_str] = country_cap

# here, the loop variable. holding the user decision is passed to the function
loop = input('do you want to enter another country (y/n) : ')
while(check_input(loop) == False):
    loop = input('do ou want to enter another country(y/n) :')

    if loop == 'n':
        break

# list is made to hold the country and capital
value_key_list = []
for key, val in capitals.items():
    value_key_list.append((key,val))
value_key_list.sort()

for val, key in value_key_list:
    print(key, ': ', val)


