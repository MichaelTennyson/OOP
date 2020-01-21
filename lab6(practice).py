import string

def make_dict():
    open_file = open('gettysburg.txt', 'r')
    stop_file = open('stopwords.txt', 'r')
    stopwords = stop_file.read().splitlines()

    dict_1 = {}
    for line in open_file:
        line = line.lower()
        line = line.split()
        for w in line:
            if w in stopwords:
                continue
            w = w.strip(string.punctuation)
            w = w.strip(string.whitespace)
            add_to_dict(w, dict_1)
        open_file.close()
        return dict_1


def add_to_dict(word, dict):
    for key in dict.keys():
        if key == word:
            dict[key] += 1
        else:
            dict[word] = 1
            return dict

# the html function prints out

def html_file(dict):
    file_html = open('html_file.html', 'w')
    file_html.write('<!DOCTYPE html>\
    <html>\
    <head lang="en">\
    <meta charset="UTF-8">\
    <title>Tag Cloud Generator</title>\
    </head>\
    <body>\
    <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">')

    for key in dict.keys():
        file_html.write('<span style="font-size: ')
        file_html.write(str(dict[key]*10))
        file_html.write('px"> ')
        file_html.write(key)
        file_html.write('</span>')


    file_html.write('</div>\
    </body>\
    </html>')

# function calls
dict_1 = make_dict()
html_file(dict_1)