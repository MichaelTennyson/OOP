# the following program will combine to two dictionaries into one

dict_a = {'a': 100, 'b': 200, 'c': 300}
dict_b = {'a': 300, 'b': 200, 'd': 400}
dict_c = {}

for key in dict_a:
    dict_c[key] = dict_a[key]


for key in dict_b:
    if key in dict_a.keys():
        dict_c[key] += dict_b[key]
    else:
        dict_c[key] = dict_b[key]

print(dict_c)


