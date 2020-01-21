# this program checks if a sentence entered is a heterogram or not
def heterogram(sentence):
    sentence_list = list(sentence)

    # ord function returns ascii version of character
    alphabet = [ch for ch in sentence_list if(ord(ch) >= ord('a') and ord(ch) <= ord('z'))]
    sentence_set = set(sentence_list)

    if len(sentence_set) == len(alphabet):
        print('yes, your word is a hectogram')
    else:
        print('no, your word is not a hectogram')


print('enter a word that does not use a letter more than twice(hectogram)')