# * Reverse a String - Enter a string and the program will reverse it and print it out.
# Also rev sentences but not words in them
# if str is longer than one word reverse the order else reverse the single word

def reverser():
    str = input("Give me a string to reverse: ")
    if len(str.split()) > 1:
        rev_sent = (' '.join(str.split()[::-1]))
        print(rev_sent)
    else:
        revstr = str[::-1]
        print(revstr)
    reverser()

reverser()