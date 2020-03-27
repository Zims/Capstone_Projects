# * Count Vowels - Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.
from collections import Counter



user_input = input('Write a text and I will count the vowels: ')
# print(f'You chose this text: {user_input}')
lowecase_input = user_input.lower()

def vowel_counter(lowecase_input):

    

    vowel = ['a', 'e', 'i', 'o', 'u']
    final = [each for each in lowecase_input if each in vowel]
    
    print(f'I counted {len(final)} vowels!')
    # print(final)
    print(Counter(final))
    print('Press Ctrl + C to exit. Or')
    user_input = input('write a text and I will count the vowels: ')
    lowecase_input = user_input.lower()
    vowel_counter(lowecase_input)

vowel_counter(lowecase_input)


