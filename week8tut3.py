dict_b = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven','8':'eight', '9':'nine', '0':'zer0'}

num = input('enter a number\n')
dict_keys = dict_b.keys()

for char in num:
    if char in dict_keys:
        print(dict_b[char],end='')
    else:
        print('you must enter a number')