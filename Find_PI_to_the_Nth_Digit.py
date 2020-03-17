pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
after_comma = int(input(f"How many numbers after the dot do you want? "))

def upTo(after_comma):
    result = round(pi, after_comma)
    print(result)



upTo(after_comma)
