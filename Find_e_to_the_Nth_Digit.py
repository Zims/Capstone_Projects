# Find e to the Nth Digit - 
# Just like the previous problem, 
# but with e instead of π (pi). Enter a number and have the program generate e 
# up to that many decimal places. Keep a limit to how far the program will go.

import random
e = round(random.random(), 100)

def upTo():
    after_comma = None

    while type(after_comma) != int:
        try:
            after_comma = int(input(f"How many numbers after the dot do you want? "))
        except ValueError:
                    print('Sorry, a bet must be an number!')
        else:
            result = round(e, after_comma)
            print(f'Here is pi with {after_comma} numbers after the dot: {result}')
            upTo()

upTo()