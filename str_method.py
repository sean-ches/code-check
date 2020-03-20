import re

# String to look for
string = 'Is this a program? Yes, it is one, it will count how many: colons, commas, dots, and question marks are in the string.'

split_str = re.findall(r"[\w']+", string)
print(split_str)
# Count length of string
print('Length of string:', len(string), '\nAmount of words:', len(split_str))

# Count specific things in string
print('---------------------------------')
print('Amount of dots:', string.count('.'))
print('Amount of commas:', string.count(','))
print('Amount of spaces:', string.count(' '))
print('Amount of colons:', string.count(':'))
print('Amount of question marks:', string.count('?'))
print('---------------------------------\n')

# Count "a" "an" and "the" in sentence
print('Amount of "a" in sentence: ', split_str.count('a'))
print('Amount of "an" in sentence: ', split_str.count('an'))
print('Amount of "the" in sentence: ', split_str.count('the'))

# Find biggest word
length_of_word = 0
for word in split_str:
    if len(word) > length_of_word:
        length_of_word = len(word)
        biggest_word = word
print('Biggest word in the sentence is:', biggest_word)







