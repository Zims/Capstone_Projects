# * Count Words in a String - Counts the number of individual words in a string. 
# For added complexity read these strings in from a text file and generate a summary.


given_string = 'this is so heavy'

string_to_list = given_string.split()
print(len(string_to_list))

f = open("/Users/zims/Desktop/count_me.txt", "r")
string_from_file = (f.read())
list_from_file = string_from_file.split()
word_in_file = len(list_from_file)
print(f'The file contains {word_in_file} words')

