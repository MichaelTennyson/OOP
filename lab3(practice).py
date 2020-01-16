# The following program scrambles a string, leaving the first  and last letter be
# the user first inputs their string
# the string is then turned into a list and is split apart
# the list of characters are scrambled and concatenated

import random

print("this program wil take a word and will scramble it \n")
word = input("enter the word\n")

word_list = list(word)

for i in range(len(word_list)):
    random.shuffle(word_list[1:-1])

scrambled_word = "".join(word_list)

print(scrambled_word)
