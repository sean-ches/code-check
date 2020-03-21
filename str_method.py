import re

# Handle sentences file
file = open('random sentences.txt')

# First word list
first_word = []

for string in file:

    # Splits
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
    print('Amount of "a" in sentence:', split_str.count('a'))
    print('Amount of "an" in sentence:', split_str.count('an'))
    print('Amount of "the" in sentence:', split_str.count('the'))

    # Find biggest word
    length_of_word = 0
    for word in split_str:
        if len(word) > length_of_word:
            length_of_word = len(word)
            biggest_word = word
    print('Biggest word in the sentence is:', biggest_word)



    print('\nFirst word in sentence is:', split_str[0])
    first_word.append(split_str[0])


print('\n\nAdditional data:\n')

# First words: Biggest
length_of_first_word = 0
for word in first_word:
    if len(word) > length_of_first_word:
        length_of_first_word = len(word)
        biggest_first_word = word


print('Biggest first word is:', biggest_first_word)

# First words: no space string


print(''.join(first_word))







