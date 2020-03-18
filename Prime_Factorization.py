# Prime Factorization - Have the user enter a number and 
# find all Prime Factors (if there are any) and display them.

# https://www.khanacademy.org/math/pre-algebra/pre-algebra-factors-multiples/pre-algebra-prime-factorization-prealg/v/prime-factorization-exercise

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
factor_num = int(input('I want to do prime factorization on: '))
factor_list = []


def loop():
    for prime in prime_list:
        if factor_num % prime == 0:
            factor_list.append(prime)


            
def factorize():
    if factor_num not in prime_list:
        loop()

    else:
        print(f'{factor_num} is prime AF')

factorize()
print(factor_list)