import random

#function imports list to scramble the word
def scramble(txt):
   l = list(txt)
   random.shuffle(l)
   return ''.join(l)

#function to check if the word is greater than 3
def garble_txt(txt):
   if len(txt) <= 3:
      return txt

   #splits word apart into first letter, midlle letters and last
   first_l, middle_l, last_l = txt[0], txt[1:-1] , txt[-1]

   return first_l + scramble(middle_l) + last_l

def garble(sentence):
   words = sentence.split(' ')
   return ' '.join(map(garble_txt, words))


str = input("enter some words\n")
scramble_word = scramble(str)
scramble_word = garble_txt(str)
scramble_word = garble(str)
print(scramble_word)