# date 07/10/2019
# author - Michael Tennyson
# the code is a game that asks users to input two syllables
# the two syllables will be added to the word to make the word gibberish
# if the user enters and astrix and a letter to be added.
# the astrix will be replaced by a vowel in the word
# the user can then enter what word they want to be turned to gibberish

import string

count = True

while count == True:
    print("Welcome to the gibberish game\n")
    print("this game turns a word you enter into gibberish\n")
    print("But first you must make a syllable to add to the word\n")
    print("if you want to add a syllable with the vowel from your word, enter an'*'with the letter\n")
    print( "or if you want to add the brand new syllable you would like gito add to your word add an astrix(*) alongside your syllable\n")
    syl1 = input("enter the first syllable you want to have added to your word\n")
    syl2 = input("enter the second syllable to be added to your word\n")
    word = input("now enter the word you want to be turned to gibberish\n")
    numbers = "0123456789"
    vowels = "aeiouAEIOU"

    # the following code splits the string into separate characters
    syll_list = list(word)

    Gibberish_present = False
    double_vowel_checker = False
    number_checker = False
    syl_vowel_check = False

    syl_separate1 = list(syl1)
    syl_separate2 = list(syl2)

    # checking if the first syllable has a numbers
    for i in range(len(syl_separate1)):
        if syl_separate1[i] in numbers:
            number_checker = True
            print("You have a number in your 1st syllable, you cannot have numbers in your syllable\n")
        else:
            number_checker = False
            syl1 = ''.join(syl_separate1)
    # checking if the second syllable has a number
    for i in range(len(syl_separate2)):
        if syl_separate2[i] in numbers:
            number_check = True
            print("you have a number in your 2nd syllable\n")

        else:
            number_checker = False
            syl2 = ''.join(syl_separate2)

    # the following code checks the length of both syllables
    syllen = 'abc'
    syllen_1 = list(syl1)
    syllen_2 = list(syl2)

    for i in range(len(syllen_1)):
        if len(syllen_1[i]) >= len(syllen):
            print("Your first syllable has more than two letters\n")

    for i in range(len(syllen_2)):
        if len(syllen_2[i]) >= len(syllen):
            print("Your secon syllable has more than two letters")


    # wild card code
    astrix_checker1 = list(syl1)
    astrix_checker2 = list(syl2)
    ast_check = False

    for i in range(len(syll_list)):
        for j in range(len(astrix_checker1)):
            if astrix_checker1[0] == '*':
                astrix_checker1[0] = syll_list[i] in vowels

    for i in range(len(syll_list)):
        for j in range(len(astrix_checker2)):
            if astrix_checker2[0] == '*':
                astrix_checker2[0] == syll_list[i] in vowels

    # the following code is responsible for inserting syllables
    for i in range(len(syll_list)):
        if syll_list[i] in vowels and double_vowel_checker == False:
            if Gibberish_present == False:
                double_vowel_checker = True
                Gibberish_present = True
                syll_list[i] = syl1 + syll_list[i]
            else:
                syll_list[i] = syl2 + syll_list[i]
                double_vowel_checker = True
        else:
            if syll_list[i] not in vowels:
                double_vowel_checker = False

    new_word = ''.join(syll_list)
    print("your word in gibberish is ", new_word)

    decision = input("do you want to play again? - (y/n)\n")

    if decision == "y":
        count = True
    if decision == "n":
        count = False

# end of code















