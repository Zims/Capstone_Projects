


pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286


def upTo():
    after_comma = int(input(f"How many numbers after the dot do you want? "))


    result = round(pi, after_comma)
    print(f'Here is pi with {after_comma} numbers after the dot: {result}')


upTo()
