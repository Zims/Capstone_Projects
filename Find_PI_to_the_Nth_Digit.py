# **Find PI to the Nth Digit**

#  - Enter a number and have the program generate &pi; (pi) up to that many decimal places. Keep a limit to how far the program will go.


pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286


def upTo():
    after_comma = None

    while type(after_comma) != int:
        try:
            after_comma = int(input(f"How many numbers after the dot do you want? "))
        except ValueError:
                    print('Sorry, a bet must be an integer!')
        else:
            result = round(pi, after_comma)
            print(f'Here is pi with {after_comma} numbers after the dot: {result}')
            upTo()

upTo()
