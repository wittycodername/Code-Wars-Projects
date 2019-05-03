
# 7 kyu Vowel Count

def getCount(inputStr):
    num_vowels = 0
    for letter in inputStr:
       if letter in ['A', 'E', 'I', 'O', 'U','a', 'e', 'i', 'o', 'u']:
           num_vowels += 1
    return num_vowels